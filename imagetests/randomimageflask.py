from flask import Flask, render_template, request
#import noaaClimateData as noaa
#import mngeoservices as mngeo
from PIL import Image
import rasterio
import json
import os
#import numpy as np

newdir = f'.\\randomimages'
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

@app.route('/saveimages', methods=['GET', 'POST'])
def saveimages():
    if request.method=='POST':
        bytes = request.files['image']
        im = Image.open(bytes)
        #bytes = im.tobytes()
        image = Image.frombytes(mode='RGB', size=[1000, 1000], data=im)
        data = json.load(request.files['data'])
        #size = request.json['size']
        #im = rasterio.open(image)
        #im = Image.open(image)
        #bytes = im.tobytes()
        image.save(f'.\\randomimages\\{data['filename']}')
        return {'response':f'{bytes[0:100]}\n{sum(bytes)}'}