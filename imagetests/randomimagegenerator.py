'''
Written by Alec Olson
Last edited 08/05/2024

A script to generate random images and send them to a web app, which will then save those images to disk.

The first loop in this script generates random images and saves them to disk. The number of images to generate and the size of these images can be adjusted by changing the 'num' and 'dimension' variables, respectively.
    These images are stored in a new directory titled 'createrandomimages'.

The second loop in this script opens up each image and sends a POST request to a Flask endpoint, described in 'randomimageflask.py', along with a json file containing the name of the image.
    This loop also records the time taken to send each image to the endpoint, and all this information is then consolidated in a csv file titled 'randomimagetimes<dimension>', where <dimension> is the number of pixels on one side of the image.

'''


import numpy as np
from PIL import Image
import sys
import os
import requests
import time
import json

timelist = []

newdir = f'.\\createrandomimages'
if not os.path.exists(newdir):
    os.makedirs(newdir)

num = 5        # number of images to generate
dimension = 1000    # number of pixels on each side of the image
                    # 1000 x 1000 results in images that are 550-590 KB, throughput as high as 15 images/sec
                    # 2000 x 2000 resulst in images that are 2.1 - 2.3 MB, throughput around 4-5 images/sec
                    # 4000 x 4000 results in images that are 8.5 - 9.2 MB,
                    # 5000 x 5000 results in images that are 13.3 - 14.3 MB, throughout around 0.333 images/sec

# generate num number of random images of dimension size
for i in range(num):
    array = np.random.randint(0, 256, size=(dimension, dimension, 3))
    im = Image.fromarray(array.astype('uint8')).convert('RGB')
    im.save(f'.\\createrandomimages\\randomtestimage{i}.jpeg')

# send each image to the Flask endpoint and time how long this process takes for each image
for i in range(num):
    start_time = time.time()
    #im = Image.open(f'.\\createrandomimages\\randomtestimage{i}.jpeg')
    #bytes = im.tobytes()
    filename = 'randomtestimage' + str(i) + '.jpeg'
    filepath = f'.\\createrandomimages\\randomtestimage{i}.jpeg'
    data_dict = {}
    data_dict['filename'] = filename
    with open('randomimagedata.json', 'w') as fp:
        json.dump(data_dict, fp)
    
    # #this always returns the same bytestream
    # with open(filepath, 'rb') as image:
    #     data = image.read()
    #     print(data[0:100])

    with open(filepath, 'rb') as image:
        response = requests.post('http://127.0.0.1:5000/saverandomimages', files={'image': image, 'data': open('randomimagedata.json', 'r')})    # open the image here
        #data = image.read()
        #print(data[0:100])
        print(response.text)
        print(response.status_code)
    print()
    end_time = time.time()
    timelist.append([end_time - start_time, response.text])

# create a csv file with the time for each image
with open(f'cloudrandomimagetimes{dimension}.csv', 'w') as fp:
    fp.write(f'script, flask\n')
    for i in range(len(timelist)):
        fp.write(f'{timelist[i][0]}, {timelist[i][1]}\n')

# for i in range(1):
#     print(os.stat(f'testimage{i}.jpeg').st_size)

# im = Image.open(f'testimage0.jpeg')
# bytes = im.tobytes()
# bytes = sys.getsizeof(im.tobytes())
# print(bytes)
# response = requests.post('http://127.0.0.1:5000/saveimages', files={'image': open('testimage0.jpeg', 'rb')})
# #response2 = requests.post('http://127.0.0.1:5000/saveimages', json={'size': bytes})
# # print(response)
# # print(response.reason)
# print(response.text)
#print(response2.text)

# headers={'Content-Type': 'application/json'}