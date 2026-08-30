import cv2
import numpy as np

# Load the image
image = cv2.imread("/home/pinal-gadhiya/Downloads/Pinal-backup/Pinal Gadhiya/Digital_Signal & Image_Processing/Lab_Exp_9/median_filt.jpeg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Define the size of the median filter kernel
# It should be an odd number
kernel_size = 5

# Apply the Median filter for smoothing
smoothed_image = cv2.medianBlur(image, kernel_size)

# Display the original and smoothed images
cv2.imshow("Original Image", image)
cv2.imshow("Smoothed Image - Median Filter", smoothed_image)

cv2.waitKey(0)
cv2.destroyAllWindows()