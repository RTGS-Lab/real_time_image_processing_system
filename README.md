# Realtime Spatial Image Processing System
Prototype system for spatial image processing able to hand aerial and oblique views.

This project will pull real-time aerial and satellite imagery, store metadata about these images in a database, and save the images to disk.

Navigation:
- The apis directory contain two Python scripts `mngeoservices.py` and `noaaClimateData.py`, that request satellite imagery and climate data, respectively, from Minnesota Geospatial Image Service and NOAA. This directory also contains a Flask script, flaskdemo.py, that receives images at an endpoint and returns the first 100 bytes of those images.
- The imagetests directory contains four Python scripts. 
    - randomimagegenerator.py generates images based on random numpy arrays and saves those images to disk.
    - tiftest.py takes a tif file, creates a json file with the metadata from the tif, and sends both bytestreams to a Flask endpoint.
    - mngeoservices.py repeatedly requests satellite imagery from the MN Geospatial Image Service, creates a json file with the metadata for each image, and sends both the image and the json file to a Flask endpoint.
    - flaskdemo.py creates an endpoint that receives the images sent to it by mngeoservices.py, and this endpoint saves the images to disk.
    - time.csv and timedistribution.Rmd take the amount of time that mngeoservices.py takes to receive each image from the MN Geospatial Image Service and demonstrates that there is no significant relationship between the file size of the image and the amount of time it takes for the Python script to receive it and send it to the Flask endpoint.

Expected Technical Challenges:
- Throughput of images pulled from the API has the potential to be higher than the throughput of analyzing them. This would create a backlog in the program, and it would eventually overwhelm memory.
- Large image file size, or a large quantity of images, or a combination of the two, may require large amounts of space in order to store them all.
- Spatial resolution and spatial extent may vary among the images, which will require a flexible program to be able to analyze all of them.
- Not all data entering the program is guaranteed to be an image.
- Image data may be corrupted in some way, with incorrect or missing coordinates, time stamps, or attribute data.
- Not all images may be useful or desired. There may have to be a way to sort out which images have little or no value to the project.
- If collecting images from multiple sources, there may be differences in file formats, documentation, or attribute data, so a program that works for one source of images may not work perfectly for another source.

Link to Google Drive folder:
https://drive.google.com/drive/folders/1-9JLfV14hQm7SkclQHYk9m-S93KJrZm7

Contributors:
- Alec Olson
- Dr. Bryan Runck
