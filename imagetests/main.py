import os
from flask import Flask, request
from PIL import Image
import json
import time

app = Flask(__name__)

newdir = f'.\\savedimages'      # for mngeoservices.py
if not os.path.exists(newdir):
    os.makedirs(newdir)

newdir = f'.\\saverandomimages'     # for randomimagegenerator.py
if not os.path.exists(newdir):
    os.makedirs(newdir)

@app.route("/")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello again {name}!"

@app.route("/goodbye")
def table():
    return "Goodbye"

@app.route('/saveimages', methods=['GET', 'POST'])
def saveimages():
    if request.method=='POST':
        start_time = time.time()
        image = request.files['image']
        data = json.load(request.files['data'])
        #size = request.json['size']
        #im = rasterio.open(image)
        im = Image.open(image)
        bytes = im.tobytes()
        #filename = 'doesthiswork' + str(size) + '.jpeg'
        im.save(f'.\\savedimages\\{data['filename']}')
        #print(bytes[0:100])
        # image_name = f'{image.filename}testing'
        # image.save(image_name.tobytes())
        end_time = time.time()
        return f'{data['filename']} {end_time - start_time}'
        return {'response':f'{bytes[0:100]}'}

@app.route('/saverandomimages', methods=['GET', 'POST'])
def saverandomimages():
    if request.method=='POST':
        # right now, this endpoint is just testing to verify that it is receiving the image properly
        # it returns the first 100 bytes of the image that it received, and this is compared to the printout of the first 100 bytes that randomimagegenerator produces before it sends the image

        #start_time = time.time()
        bytes = request.files['image']
        data = bytes.read()
        #im = Image.open(bytes)
        #bytes = im.tobytes()
        #image = Image.frombytes(mode='RGB', size=[1000, 1000], data=im)
        #data = json.load(request.files['data'])
        #size = request.json['size']
        #im = rasterio.open(image)
        #im = Image.open(image)
        #bytes = im.tobytes()
        return f'{data[0:100]}'
        #im.save(f'.\\saverandomimages\\{data['filename']}')
        #end_time = time.time()
        #total_time = end_time - start_time
        #return str(total_time)
        #return f'{bytes[0:100]}'



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))