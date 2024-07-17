The imagetests directory contains four Python scripts. 
- `randomimagegenerator.py` generates images based on random numpy arrays and saves those images to disk.
- `tiftest.py` takes a tif file, creates a json file with the metadata from the tif, and sends both bytestreams to a Flask endpoint.
- `mngeoservices.py` repeatedly requests satellite imagery from the MN Geospatial Image Service, creates a json file with the metadata for each image, and sends both the image and the json file to a Flask endpoint.
- `flaskdemo.py` creates an endpoint that receives the images sent to it by `mngeoservices.py`, and this endpoint saves the images to disk.

`time.csv` and `timedistribution.Rmd` take the amount of time that mngeoservices.py takes to receive each image from the MN Geospatial Image Service and demonstrates that there is no significant relationship between the file size of the image and the amount of time it takes for the Python script to receive it and send it to the Flask endpoint.