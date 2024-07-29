# APIS

Navigation:
- This directory contains two Python scripts `mngeoservices.py` and `noaaClimateData.py`, that request satellite imagery and climate data, respectively, from Minnesota Geospatial Image Service and NOAA. This directory also contains a Flask script, `flaskdemo.py`, that receives images at an endpoint and returns the first 100 bytes of those images.

- `noaaClimateData.py` contains a function that requests yearly climate data from NOAA and takes as its input a list of years for which the user wants data. Then, the function creates a csv file to display that data and converts the csv file to an html file so that it will be viewable on a web app.
- `mngeoservices.py` requests a satellite image of the north shore of Minnesota from the Minnesota Geospatial Image Service and save this image to disk.
- `flaskdemo.py` is setup to have an endpoint accept POST requests from Postman, an API testing software. Once the endpoint receives the image, it will save the image to disk and return the first 100 bytes of the image to double check that it has received the image properly.
