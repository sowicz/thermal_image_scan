import cv2
import numpy as np


class ThermalImageGrid:
    def __init__(self, image, grid_size):
        self.image = image
        self.grid_size = grid_size
        self.height, self.width = image.shape[:2]

    def draw_grid_on_color(self, lower_temp, upper_temp, color):
        # Create a mask that selects pixels within the specified range
        mask = cv2.inRange(self.image, lower_temp, upper_temp)

        # Apply mask 
        filtered_image = cv2.bitwise_and(self.image, self.image, mask=mask)
        cv2.imshow('Filtered Image', filtered_image)

        # Loop over the grid cells 
        for y in range(0, self.height, self.grid_size[0]):
            for x in range(0, self.width, self.grid_size[1]):
                # Define the region of interest (ROI) for the current grid cell
                roi = mask[y:y + self.grid_size[0], x:x + self.grid_size[1]]

                # Calculate the percentage of white pixels in the mask (i.e., pixels within the color range)
                percentage_white = np.sum(roi == 255) / (self.grid_size[0] * self.grid_size[1]) * 100

                # Define a threshold for determining whether the grid cell should be highlighted
                threshold = 0.5  # For example, highlight if at least 20% of the grid cell is within the color range

                # Check if the percentage of white pixels exceeds the threshold
                if percentage_white > threshold:
                    # Draw a rectangle around the grid cell
                    cv2.rectangle(self.image, (x, y), (x + self.grid_size[1], y + self.grid_size[0]), color, 2)
        
        return self.image

    def display_image(self, window_name):
        cv2.imshow(window_name, self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


#---------------------------------------------------------
# Load your image
image = cv2.imread('thermal_image.jpg')
image2 = cv2.imread('thermal_image.jpg')
# image = cv2.imread('thermal_img2.jpg')



#---------------------------------------------------------
# Draw temperature gradient
topL = (10,80)
botR = (20,300)
rect_height = botR[1] - topL[1]
rect_width = botR[0] - topL[0]

# Create a vertical gradient grayscale image for the rectangle
gradient = np.linspace(255, 0, rect_height, dtype=np.uint8)  # Reverse the gradient
gradient = np.tile(gradient[:, np.newaxis], (1, rect_width))

colored = cv2.applyColorMap(gradient, cv2.COLORMAP_JET)
# white border
cv2.rectangle(image2, topL, botR, (255, 255, 255), thickness=3)

# image_color = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
image2[topL[1]:botR[1], topL[0]:botR[0]] = colored


# show original img
cv2.imshow('Original', image2)


#---------------------------------------------------------
# Define the grid size (height, width) of each cell
grid_size = (100, 100)


#---------------------------------------------------------
# Define lower and upper bounds for the color range (in HSV)
lower_temp = np.array([0, 0, 160])    # Example: Lower bound for a certain color
upper_temp = np.array([0, 40, 255])   # Example: Upper bound for the color

# Color for rectangle
color_red = (0, 0, 255)



#---------------------------------------------------------
# Create an instance of the ThermalImageGrid class
thermal_grid = ThermalImageGrid(image, grid_size)

# Draw the grid and highlight cells based on color range
result_image = thermal_grid.draw_grid_on_color(lower_temp, upper_temp, color_red)

# Display the result
thermal_grid.display_image('Grid with Highlighted Cells')


