'''
Written by Alec Olson
Last edited 08/05/2024

A script to pull satellite imagery from the MN Geospatial Image Service and send those images to a web app, which will then save the images to disk.

Function:
    - image(xmin, xmax, ymin, ymax)
        - This function takes a min and max x coordinate and y coordinate and retreives a satellite image corresponding to this spatial extent
        - The coordinates are in NAD83 / UTM zone 15N
        - The MN Geospatial Image Service provides public access to many image repositories, but this script is setup to retrieve images of either the north shore of Lake Superior, in Minnesota, or the south shore of the lake, in Wisconsin.

The main body of this script makes repeated calls to the image function in order to receive many satellite images. For each image, this script creates a dictionary that contain's the images coordinates,
and then that dictionary is turned into a json file. Next, this script makes a POST request to a web app, described in flaskdemo.py, and sends the image and its json file.
Addtionally, this script records the total amount of time that this whole process takes for each image, in order to allow for analysis on the effect between time and file size of the image.      
'''


import requests
import time
import os
import json

# baseURL = 'https://imageserver.gisdata.mn.gov/cgi-bin/wms?VERSION=1.3.0&SERVICE=WMS&'
# continuedURL = 'REQUEST=GetMap&LAYERS=fsa2021&STYLES=&srs=EPSG%3A4326'

def image(xmin, xmax, ymin, ymax):
    width = 400
    height = (ymax - ymin) / (xmax - xmin) * 400
    # Only use one of the following two lines. Leave the other one commented out.
    #response = requests.get(f'https://imageserver.gisdata.mn.gov/cgi-bin/wms?VERSION=1.3.0&SERVICE=WMS&REQUEST=GetMap&LAYERS=dulir09&STYLES=population&CRS=EPSG%3A26915&BBOX={xmin},{ymin},{xmax},{ymax}&width={width}&height={height}&format=image/jpeg')      # use this line to request images of the north shore of Lake Superior
    response = requests.get(f'https://imageserver.gisdata.mn.gov/cgi-bin/wms?VERSION=1.3.0&SERVICE=WMS&REQUEST=GetMap&LAYERS=wisc09&STYLES=population&CRS=EPSG%3A26915&BBOX={xmin},{ymin},{xmax},{ymax}&width={width}&height={height}&format=image/jpeg')      # use this line to request images of the south shore of Lake Superior
    if response.status_code == 200:
        return response.content
    else:
        print(f'Error retreiving image, status code {response.status_code}')
        return None

# 542462.7,5163473.7,595449.6,5233922.4 Duluth north shore          # These are the bounding coordinates for the north shore imagery
# minx="602935.2" miny="5143471.2" maxx="730540.8" maxy="5223000" Wisconsin south shore             # These are the bounding coordinates for the south shore imagery

# xcors = list(range(575000, 580001, 1000))     Duluth coordinates          # Uncomment out these two lines if you are requesting north shore imagery. Then, comment out the lines below that correspond to the south shore imagery.
# ycors = list(range(5195000, 5200001, 1000))   Duluth coordinates          # The third parameter in each of these lists is the size, in meters, of each side of each image (ex. 1000 means that each image will be 1000 x 1000m in spatial extent).

# The third parameter in each of these lists is the size, in meters, of each side of each image (ex. 5000 means that each image will be 5000 x 5000m in spatial extent).
#   Adjust this number if you desire larger or smaller images.
#   Smaller image sizes will result in a higher quantity of images being saved.
xcors = list(range(650000, 680001, 5000))       # Wisconsin south shore coordinates
ycors = list(range(5180000, 5210001, 5000))     # Wisconsin south shore coordinates
timelist = []
datalist = []

count = 100     # start count at 0 for Duluth; start count at 100 for Wisconsin. This variable just helps with creating the filename for each image.
for i in range(len(xcors)-1):
    for j in range(len(ycors)-1):
        start_time = time.time()
        xmin = xcors[i]
        xmax = xcors[i+1]
        ymin = ycors[j]
        ymax = ycors[j+1]
        result = image(xmin, xmax, ymin, ymax)
        if result != None:
            filename = 'testimage' + str(count) + '.jpeg'
            data_dict = {}
            data_dict['filename'] = filename
            #data_dict['bytes'] = bytes
            data_dict['coordinates'] = {}
            data_dict['coordinates']['xmin'] = xmin
            data_dict['coordinates']['xmax'] = xmax
            data_dict['coordinates']['ymin'] = ymin
            data_dict['coordinates']['ymax'] = ymax
            datalist.append(data_dict)
            with open('data.json', 'w') as fp:
                json.dump(data_dict, fp)
            with open('data.json', 'r') as datafile:
                response = requests.post('http://127.0.0.1:5000/saveimages', files={'image': result, 'data': datafile})    # open the image here
                print(response.content)
        count += 1
        end_time = time.time()
        timelist.append([bytes, end_time - start_time])

print(timelist)
with open('time2.csv', 'w') as fp:
    fp.write('bytes,time\n')
    for time in timelist:
        fp.write(f'{time[0]},{time[1]}\n')

# Create a json file containing metadata for every single image that has just been received.
with open('metadata.json', 'w') as fp:
    json.dump(datalist, fp)


#print(datalist)

# with open('data.json', 'w') as fp:
#     json.dump(data_dict, fp)
