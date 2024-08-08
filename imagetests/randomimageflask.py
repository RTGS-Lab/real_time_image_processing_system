'''
Written by Alec Olson
Last edited 08/05/2024

A script to create a web app to receive images and save those images to disk.

Endpoints
    - /saveimages
        - This endpoint is setup to receive POST requests that contain two files: an image in binary mode and a json file containing the image's metadata.
        - This endpoint then saves that image to disk in a new directory titled 'saverandomimages', and the filename of that image is determined by the information in the json file.
        - This endpoint records how much time this whole process takes and returns this time to the script that sent the POST request.

'''


from flask import Flask, render_template, request
#import noaaClimateData as noaa
#import mngeoservices as mngeo
from PIL import Image
import rasterio
import json
import os
import time
#import numpy as np

newdir = f'.\\saverandomimages'
if not os.path.exists(newdir):
    os.makedirs(newdir)

app = Flask(__name__)

# @app.route('/')
# def main(name=None):
#     return render_template(filename, name=name)

# @app.route('/index')
# def index():
#     return render_template('index.html')

# @app.route('/images')
# def images():
#     return render_template('htmlpractice.html')

@app.route('/saverandomimages', methods=['GET', 'POST'])
def saverandomimages():
    if request.method=='POST':
        start_time = time.time()
        bytes = request.files['image']
        im = Image.open(bytes)
        #bytes = im.tobytes()
        #image = Image.frombytes(mode='RGB', size=[1000, 1000], data=im)
        data = json.load(request.files['data'])
        #size = request.json['size']
        #im = rasterio.open(image)
        #im = Image.open(image)
        #bytes = im.tobytes()
        im.save(f'.\\saverandomimages\\{data['filename']}')
        end_time = time.time()
        total_time = end_time - start_time
        return str(total_time)