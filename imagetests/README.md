### The imagetests directory contains four Python scripts that are divided into two categories.

#### Category 1: Receiving images from the MN Geospatial Image Service
- `mngeoservices.py` repeatedly requests satellite imagery of the south shore of Lake Superior from the MN Geospatial Image Service, creates a json file with the metadata for each image, and sends both the image and the json file to a Flask endpoint created in 'flaskdemo.py'
- `flaskdemo.py` creates a local Flask endpoint that receives the images sent to it by `mngeoservices.py`, and this endpoint saves the images to disk in a new directory titled `flaskimages`.
##### How to run these files
- First, begin running `flaskdemo.py` in your terminal.
```
flask --app flaskdemo run
```
- Next, open `mngeoservices.py` in an IDE of your choice. The spatial extent and the image dimensions can be adjusted inside this script. Next, run the program from the IDE.

More information regarding the MN Geospatial Image Service can be found in this GetCapabilities XML file:
https://imageserver.gisdata.mn.gov/cgi-bin/wms?VERSION=1.3.0&SERVICE=WMS&REQUEST=GetCapabilities

#### Category 2: Generating random images
- `randomimagegenerator.py` generates images based on random numpy arrays and sends them to the Flask endpoint created in 'randomimageflask.py'. These images are initially stored in a new directory titled `createrandomimages` before they are sent to the endpoint.
- `randomimageflask.py` creates a local Flask endpoint that receives the images sent to it by `randomimagegenerator.py`, and this endpoint saves the images to disk in a new directory titled `saverandomimages`.
##### How to run these files
- First, begin running `randomimageflask.py` in your terminal.
```
flask --app randomimageflask run
```
- Next, open `randomimagegenerator.py` in an IDE of your choice. The number of images and the dimension of these images can be adjusted inside this script. Next, run the program from the IDE.

#### Throughput Analysis
- `time.csv` and `timedistribution.Rmd` take the amount of time that `mngeoservices.py` takes to receive each image from the MN Geospatial Image Service and demonstrates that there is no significant relationship between the file size of the image (between 6 and 28 MB) and the amount of time it takes for the Python script to receive it and send it to the Flask endpoint.
- `randomimagegenerator.py` records the amount of time it takes to send each image to the endpoint and receive a response, and `randomimageflask.py` records the amount of time that it takes for the endpoint to receive and save each image. This information is then saved in the `randomimagetimes<num>.csv` files, where `<num>` represents the dimension of the image, i.e. 1000 means that each image is 1000 x 1000 pixels. `randomimagetimeanalysis.Rmd` shows that there is a quadratic relationship between the file size of each image (between 550 KB and 14.3 MB) and the amount of time it takes to send it to the Flask endpoint and save it. Throughput of images with dimension 1000 x 1000 is around 15 images per second, but this drops to around 1/3 image per second for images with dimension 5000 x 5000.

#### Extra script
- `tiftest.py` takes a tif file, creates a json file with the metadata from the tif, and sends both bytestreams to a Flask endpoint.


