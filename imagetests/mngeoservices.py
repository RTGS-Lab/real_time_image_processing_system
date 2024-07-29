# Connect with MN Geoservices to grab satellite imagery, save those images to disk, and create a json file to store metadata about those images

import requests
import time
import os
import json

# baseURL = 'https://imageserver.gisdata.mn.gov/cgi-bin/wms?VERSION=1.3.0&SERVICE=WMS&'

# continuedURL = 'REQUEST=GetMap&LAYERS=fsa2021&STYLES=&srs=EPSG%3A4326'

def image(xmin, xmax, ymin, ymax):
    width = 400
    height = (ymax - ymin) / (xmax - xmin) * 400
    #response = requests.get(f'https://imageserver.gisdata.mn.gov/cgi-bin/wms?VERSION=1.3.0&SERVICE=WMS&REQUEST=GetMap&LAYERS=dulir09&STYLES=population&CRS=EPSG%3A26915&BBOX={xmin},{ymin},{xmax},{ymax}&width={width}&height={height}&format=image/jpeg')      # Duluth
    response = requests.get(f'https://imageserver.gisdata.mn.gov/cgi-bin/wms?VERSION=1.3.0&SERVICE=WMS&REQUEST=GetMap&LAYERS=wisc09&STYLES=population&CRS=EPSG%3A26915&BBOX={xmin},{ymin},{xmax},{ymax}&width={width}&height={height}&format=image/jpeg')      # WI south shore of Superior
    if response.status_code == 200:
        return response.content
    else:
        print(f'Error retreiving image, status code {response.status_code}')
        #print(response.text)
        return None

# 542462.7,5163473.7,595449.6,5233922.4 Duluth north shore
# minx="602935.2" miny="5143471.2" maxx="730540.8" maxy="5223000" Wisconsin south shore
# xcors = list(range(575000, 580001, 1000))     Duluth coordinates
# ycors = list(range(5195000, 5200001, 1000))   Duluth coordinates
xcors = list(range(650000, 680001, 5000))       # Wisconsin coordinates
ycors = list(range(5180000, 5210001, 5000))     # Wisconsin coordinates
timelist = []
datalist = []

count = 100     # start count at 0 for Duluth; start count at 100 for Wisconsin
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
        count += 1
        end_time = time.time()
        timelist.append([bytes, end_time - start_time])

print(timelist)
with open('time2.csv', 'w') as fp:
    fp.write('bytes,time\n')
    for time in timelist:
        fp.write(f'{time[0]},{time[1]}\n')

with open('metadata.json', 'w') as fp:
    json.dump(datalist, fp)
    # for i in range(len(datalist)):
    #     json.dump(datalist[i], fp)

print(datalist)

# with open('data.json', 'w') as fp:
#     json.dump(data_dict, fp)

# response = requests.get(f'https://imageserver.gisdata.mn.gov/cgi-bin/wms?VERSION=1.3.0&SERVICE=WMS&REQUEST=GetMap&LAYERS=wisc09&STYLES=population&CRS=EPSG%3A26915&BBOX=650000,5180000,680000,5210000&width=1000&height=1000&format=image/jpeg')    
# output = open('C:\\Users\\ols00160\\Desktop\\project0\\static\\images\\testimage001.jpeg', 'wb')
# output.write(response.content)
# output.close()

# response = requests.get('https://imageserver.gisdata.mn.gov/cgi-bin/wms?VERSION=1.3.0&SERVICE=WMS&REQUEST=GetMap&LAYERS=neir2009&STYLES=population&CRS=EPSG%3A26915&BBOX=490342.25,5163314.75,765986.25,5392901.75&width=1000&height=833&format=image/geotiff')
# output = open('C:\\Users\\ols00160\\Desktop\\project0\\sampleimage000.tiff', 'wb')
# output.write(response.content)
# output.close()