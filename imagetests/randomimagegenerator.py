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

num = 100        # number of images to generate
dimension = 5000    # number of pixels on each side of the image
                    # 1000 x 1000 results in images that are 550-590 KB, throughput as high as 15 images/sec
                    # 2000 x 2000 resulst in images that are 2.1 - 2.3 MB, throughput around 4-5 images/sec
                    # 4000 x 4000 results in images that are 8.5 - 9.2 MB,
                    # 5000 x 5000 results in images that are 13.3 - 14.3 MB, throughout around 0.333 images/sec

# generate num number of random images of dimension size
for i in range(num):
    array = np.random.randint(0, 256, size=(dimension, dimension, 3))
    im = Image.fromarray(array.astype('uint8')).convert('RGB')
    #print(im.tobytes()[0:100])
    im.save(f'.\\createrandomimages\\randomtestimage{i}.jpeg')
    # im = Image.open(f'.\\randomimages\\randomtestimage{i}.jpeg')
    # bytes = im.tobytes()
    # #print(sum(bytes))
    # #print(bytes[0:100])
    # filename = 'randomtestimage' + str(i) + '.jpeg'
    # data_dict = {}
    # data_dict['filename'] = filename
    # #bytes = sys.getsizeof(im.tobytes())
    # with open('randomimagedata.json', 'w') as fp:
    #     json.dump(data_dict, fp)
    # #print(f'Bytes: {bytes}')            # the size of these 1000 x 1000 images is 3,000,033 bytes, which is 3 MB; however, once the images are saved, File Explorer shows that these images are 588 or 589 KB, which is only 20% the size that this line says the images are
    # response = requests.post('http://127.0.0.1:5000/saveimages', files={'image': bytes, 'data': open('randomimagedata.json', 'r')})    # open the image here
    #print(f'Kilobytes: {bytes/1000}')

# imagelist = []

# for i in range(num):
#     filepath = f'.\\createrandomimages\\randomtestimage{i}.jpeg'
#     imagelist.append(open(filepath, 'rb'))

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
    response = requests.post('http://127.0.0.1:5000/saveimages', files={'image': open(filepath, 'rb'), 'data': open('randomimagedata.json', 'r')})    # open the image here
    #print(response.text)
    end_time = time.time()
    timelist.append([end_time - start_time, response.text])

# create a csv file with the time for each image
with open(f'randomimagetimes{dimension}.csv', 'w') as fp:
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