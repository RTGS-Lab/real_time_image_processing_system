# Realtime Spatial Image Processing System
Prototype system for spatial image processing able to hand aerial and oblique views.

This project will pull satellite images from an API, analyze these images, and then store them somewhere.

Expected Technical Challenges:
- Throughput of images pulled from the API has the potential to be higher than the throughput of analyzing them. This would create a backlog in the program, and it would eventually overwhelm memory.
- Large image file size, or a large quantity of images, or a combination of the two, may require large amounts of space in order to store them all.
- Spatial resolution and spatial extent may vary among the images, which will require a flexible program to be able to analyze all of them.
- Not all data entering the program is guaranteed to be an image.
- Image data may be corrupted in some way, with incorrect or missing coordinates, time stamps, or attribute data.
- Not all images may be useful or desired. There may have to be a way to sort out which images have little or no value to the project.
- If collecting images from multiple sources, there may be differences in file formats, documentation, or attribute data, so a program that works for one source of images may not work perfectly for another source.

Contributors:
- Alec Olson
- Dr. Bryan Runck
