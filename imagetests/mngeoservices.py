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
    return response.content
    # output = open('C:\\Users\\ols00160\\Desktop\\project0\\images\\testimage2.jpeg', 'wb')
    # output.write(response.content)
    # output.close()
    # return 'testimage2.jpeg'

# 542462.7,5163473.7,595449.6,5233922.4 Duluth north shore
# minx="602935.2" miny="5143471.2" maxx="730540.8" maxy="5223000" Wisconsin south shore
# xcors = list(range(575000, 580001, 1000))     Duluth coordinates
# ycors = list(range(5195000, 5200001, 1000))   Duluth coordinates
xcors = list(range(650000, 680001, 3000))       # Wisconsin coordinates
ycors = list(range(5180000, 5210001, 3000))     # Wisconsin coordinates
timelist = []
data_dict = {}

count = 100     # start count at 0 for Duluth; start count at 100 for Wisconsin
for i in range(len(xcors)-1):
    for j in range(len(ycors)-1):
        start_time = time.time()
        xmin = xcors[i]
        xmax = xcors[i+1]
        ymin = ycors[j]
        ymax = ycors[j+1]
        result = image(xmin, xmax, ymin, ymax)
        output = open(f'C:\\Users\\ols00160\\Desktop\\project0\\images\\testimage{count}.jpeg', 'wb')
        output.write(result)
        output.close()
        bytes = os.path.getsize(f'C:\\Users\\ols00160\\Desktop\\project0\\images\\testimage{count}.jpeg')
        filename = 'testimage' + str(count) + '.jpeg'
        data_dict[filename] = {}
        data_dict[filename]['bytes'] = bytes
        data_dict[filename]['coordinates'] = {}
        data_dict[filename]['coordinates']['xmin'] = xmin
        data_dict[filename]['coordinates']['xmax'] = xmax
        data_dict[filename]['coordinates']['ymin'] = ymin
        data_dict[filename]['coordinates']['ymax'] = ymax
        count += 1
        end_time = time.time()
        timelist.append([bytes, end_time - start_time])

print(timelist)
with open('time.txt', 'w') as fp:
    fp.write('bytes,time\n')
    for time in timelist:
        fp.write(f'{time[0]},{time[1]}\n')

with open('data.json', 'w') as fp:
    json.dump(data_dict, fp)

# response = requests.get(f'https://imageserver.gisdata.mn.gov/cgi-bin/wms?VERSION=1.3.0&SERVICE=WMS&REQUEST=GetMap&LAYERS=wisc09&STYLES=population&CRS=EPSG%3A26915&BBOX=650000,5180000,680000,5210000&width=1000&height=1000&format=image/jpeg')    
# output = open('C:\\Users\\ols00160\\Desktop\\project0\\static\\images\\testimage001.jpeg', 'wb')
# output.write(response.content)
# output.close()

# response = requests.get('https://imageserver.gisdata.mn.gov/cgi-bin/wms?VERSION=1.3.0&SERVICE=WMS&REQUEST=GetMap&LAYERS=neir2009&STYLES=population&CRS=EPSG%3A26915&BBOX=490342.25,5163314.75,765986.25,5392901.75&width=1000&height=833&format=image/geotiff')
# output = open('C:\\Users\\ols00160\\Desktop\\project0\\sampleimage000.tiff', 'wb')
# output.write(response.content)
# output.close()