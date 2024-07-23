import numpy as np
from PIL import Image
import sys
import os
import requests
import time
import json

timelist = []

for i in range(0, 10):
    start_time = time.time()
    array = np.random.randint(0, 256, size=(1000, 1000, 3))
    im = Image.fromarray(array.astype('uint8')).convert('RGB')
    #print(im.tobytes()[0:100])
    im.save(f'randomtestimage{i}.jpeg')
    im = Image.open(f'randomtestimage{i}.jpeg')
    bytes = im.tobytes()
    #print(sum(bytes))
    #print(bytes[0:100])
    filename = 'randomimage' + str(i) + '.jpeg'
    data_dict = {}
    data_dict['filename'] = filename
    #bytes = sys.getsizeof(im.tobytes())
    with open('randomimagedata.json', 'w') as fp:
        json.dump(data_dict, fp)
    #print(f'Bytes: {bytes}')            # the size of these 1000 x 1000 images is 3,000,033 bytes, which is 3 MB; however, once the images are saved, File Explorer shows that these images are 588 or 589 KB, which is only 20% the size that this line says the images are
    response = requests.post('http://127.0.0.1:5000/saveimages', files={'image': bytes, 'data': open('randomimagedata.json', 'r')})    # open the image here
    end_time = time.time()
    timelist.append(end_time - start_time)
    #print(f'Kilobytes: {bytes/1000}')

print(timelist)

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