# imagetests

Navigation:
- The imagetests directory contains five Python scripts. 
    - `randomimagegenerator.py` generates images based on random numpy arrays and sends them to the Flask endpoint created in `randomimageflask.py`.
    - `randomimageflask.py` creates a Flask endpoint that receives the images sent to it by `randomimagegenerator.py`, and this endpoint saves the images to disk.
    - `mngeoservices.py` repeatedly requests satellite imagery from the MN Geospatial Image Service, creates a json file with the metadata for each image, and sends both the image and the json file to a Flask endpoint created in `flaskdemo.py`.
    - `flaskdemo.py` creates an endpoint that receives the images sent to it by `mngeoservices.py`, and this endpoint saves the images to disk.
    - `tiftest.py` takes a tif file, creates a json file with the metadata from the tif, and sends both bytestreams to a Flask endpoint.

- The `randomimagetimes<num>.csv` files contain lists of the amount of time it took for `randomimageflask.py` to receive and save the randomly generated images, where `<num>` is the pixel dimension of the (square) images.
- `randomimagetimeanalysis.Rmd` takes the above-mentioned csv files and determines that there is a quadratic relationship between image size and amount of time it takes for `randomimageflask.py` to save the images (file size ranges between 500 KB and 14 MB).

- `time.csv` and `timedistribution.Rmd` take the amount of time that `mngeoservices.py` takes to receive each image from the MN Geospatial Image Service and demonstrates that there is no significant relationship between the file size of the image and the amount of time it takes for the Python script to receive it and send it to the Flask endpoint (file size ranges between 6 and 25 MB).

## Workflow
- There are two workflows in this directory:
1. `randomimagegenerator.py` and `randomimageflask.py`
    - In the terminal, navigate to the `imagetests` directory. Begin running the Flask app by running this command:
    ```
        flask --app randomimageflask run
    ```        
    - Inside `randomimagegenerator.py`, the user can change the number of images to be generated as well as the dimension of those images. Once those parameters are set, the user can run this script. Because the terminal is being used for the Flask app, this script will need to be run from the IDE of your choice.
2. `mngeoservices.py` and `flaskdemo.py`
    - In the terminal, navigate to the `imagetests` directory. Begin running the Flask app by running this comand:
    ```
        flask --app flaskdemo run
    ```
    - Inside `mngeoservices.py`, the user can change the spatial extent of the images that will be requested from the MN Geospatial Image Service. Smaller spatial extent will result in a higher quantity of images being requested, and larger spatial extent will result in a lower quantity of images.
    - Once this parameter is set, the user can run this script. Because the terminal is being used for the Flask app, this script will need to be run from the IDE of your choice.
