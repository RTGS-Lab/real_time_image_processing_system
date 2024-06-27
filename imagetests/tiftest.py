import rasterio
import requests
import json
import numpy
from PIL import Image

image = Image.open('PlanetObserver_PlanetSAT_10m_USA_Minneapolis_UTM15.tif')
bytes = image.tobytes()
print(sum(bytes))

# fp = open('PlanetObserver_PlanetSAT_10m_USA_Minneapolis_UTM15.tif', 'rb')
# bytes = fp.read()
# print(sum(bytes))
# print(bytes[8:108])

dataset = rasterio.open('PlanetObserver_PlanetSAT_10m_USA_Minneapolis_UTM15.tif')
array = dataset.read()

# checksum = sum(sum(sum(array)))     # because each number in the array is an unsigned 8-bit int, summing up these numbers will result in a total number much smaller than the total sum due to integer overflow
                                # this should not be a problem as long as the Flask endpoint treats these numbers as unsigned 8-bit ints as well
# print(checksum)
# intchecksum = int(checksum)
# print(intchecksum)
# print(dataset.width)
# print(dataset.height)
# print(dataset.bounds)
data_dict = {}
data_dict['width'] = dataset.width
data_dict['height'] = dataset.height
data_dict['transform'] = dataset.transform
data_dict['bytes'] = sum(bytes)
# crs = dataset.crs
# print(crs.to_string)
# print(type(crs))
# print(crs)
data_dict['bounds'] = {}
data_dict['bounds']['left'] = dataset.bounds[0]
data_dict['bounds']['bottom'] = dataset.bounds[1]
data_dict['bounds']['right'] = dataset.bounds[2]
data_dict['bounds']['top'] = dataset.bounds[3]
#data_dict['checksum'] = intchecksum
# print(data_dict)
with open('data.json', 'w') as fp:
    json.dump(data_dict, fp)

# with open('data.json', 'r') as fp:
#     testing = json.load(fp)
#     print(testing)
#testing = json.loads('data.json')
#print(testing)



#response = requests.post('http://127.0.0.1:5000/saveimages', files={'image': open('PlanetObserver_PlanetSAT_10m_USA_Minneapolis_UTM15.tif', 'rb'), 'data': open('data.json', 'r')})    # open the image here
#response2 = requests.post('http://127.0.0.1:5000/saveimages', json={'image': 'PlanetObserver_PlanetSAT_10m_USA_Minneapolis_UTM15.tif'})         # send flaskdemo the name of the file, and then flaskdemo opens the image
#print(response.text)
