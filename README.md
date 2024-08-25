# thermal_image_scan


## Overview
The `thermal_image_scan` class is designed to process thermal images by overlaying a grid and highlighting specific regions based on defined temperature thresholds. This is particularly useful in thermal imaging applications where identifying regions within certain temperature ranges is crucial.

## Features
- **Grid Overlay:** Divide the image into a grid of specified cell size.
- **Color Filtering:** Highlight grid cells where the temperature falls within a specified range.
- **Customizable:** Easily adjust the grid size, temperature thresholds, and highlight color.

## Requirements
- Python 3.x
- OpenCV (`cv2`) library
- NumPy library


### Original image 
![Original image](https://github.com/sowicz/thermal_image_scan/blob/main/screenshots/Original_img.png)


### Filtered red color and make mask
![Filtered red and mask](https://github.com/sowicz/thermal_image_scan/blob/main/screenshots/filtered_Red.png)


### Grid on hottes area
![With grid](https://github.com/sowicz/thermal_image_scan/blob/main/screenshots/final_thermal.png)
