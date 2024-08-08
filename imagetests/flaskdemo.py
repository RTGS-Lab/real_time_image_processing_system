'''
Written by Alec Olson
Last edited 08/05/2024

A script to create a web app to receive images and save those images to disk.

Endpoints:
    - /
        - The 'home page', if you will. Displays "Goodbye World" to the user.
    - /saveimages
        - This endpoint is set up to recieve POST requests that contain two files: an image in binary mode, and a json file containing the image's metadata.
        - This endpoint then saves that image to disk in a new directory titled 'flaskimages', and the filename of that image is determined by the information in the json file.
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

newdir = f'.\\flaskimages'
if not os.path.exists(newdir):
    os.makedirs(newdir)

#years = list(range(2001, 2003))
#filename = noaa.getGSOY(years)
#image = mngeo.image(602935.2, 730540.8, 5143471.2, 5223000)


app = Flask(__name__)


@app.route('/')
def main():
    name = os.environ.get("NAME", "World")
    return f'Goodbye {name}'

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
        start_time = time.time()
        image = request.files['image']
        data = json.load(request.files['data'])
        #size = request.json['size']
        #im = rasterio.open(image)
        im = Image.open(image)
        #bytes = im.tobytes()
        #filename = 'doesthiswork' + str(size) + '.jpeg'
        im.save(f'.\\flaskimages\\{data['filename']}')
        #print(bytes[0:100])
        # image_name = f'{image.filename}testing'
        # image.save(image_name.tobytes())
        filesize = os.path.getsize(f'.\\flaskimages\\{data['filename']}')
        end_time = time.time()
        total_time = end_time - start_time
        return f'{str(total_time)} {str(filesize)}'

# @app.route('/image')
# def get_image(name=None):
#     return render_template(image, name=name)

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))