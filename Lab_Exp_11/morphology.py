import cv2
import numpy as np

# 1. Load the image in grayscale
image = cv2.imread('/home/pinal-gadhiya/Downloads/Pinal-backup/Pinal Gadhiya/Digital_Signal & Image_Processing/Lab_Exp_11/coins_\images.jpeg', 0)

# Check whether image is loaded successfully
if image is None:
    print("Error: Image not found. Check the image path.")
    exit()

# 2. Define the kernel (structuring element)
kernel = np.ones((5, 5), np.uint8)

# 3. Perform Erosion
erosion = cv2.erode(image, kernel, iterations=1)

# 4. Perform Dilation
dilation = cv2.dilate(image, kernel, iterations=1)

# 5. Perform Opening (Erosion followed by Dilation)
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# 6. Perform Closing (Dilation followed by Erosion)
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# 7. Display the original image and results
cv2.imshow('Original Image', image)

cv2.imshow('Erosion', erosion)

cv2.imshow('Dilation', dilation)

cv2.imshow('Opening', opening)

cv2.imshow('Closing', closing)

# 8. Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
