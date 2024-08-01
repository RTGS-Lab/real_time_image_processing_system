'''
Written by Alec Olson
Last edited 08/01/2024

Proof of concept Flask app to test simple GET and POST requests

The /saveimages endpoint is currently the only endpoint that is working. Use Postman to send images to this endpoint, and it will save the image to disk.
'''

from flask import Flask, render_template, request
#import noaaClimateData as noaa
#import mngeoservices as mngeo
from PIL import Image
#import numpy as np


# years = list(range(2001, 2003))
# filename = noaa.getGSOY(years)
#image = mngeo.image(602935.2, 730540.8, 5143471.2, 5223000)


app = Flask(__name__)


@app.route('/')
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
        image = request.files['image']
        im = Image.open(image)
        im.save('doesthiswork.jpeg')
        bytes = im.tobytes()
        #print(bytes[0:100])
        # array = np.asarray(im)
        # print(array)
        # image_name = f'{image.filename}testing'
        # image.save(image_name.tobytes())
        #print(image)
        return {"response":f"{bytes[0:100]}"}

# @app.route('/image')
# def get_image(name=None):
#     return render_template(image, name=name)