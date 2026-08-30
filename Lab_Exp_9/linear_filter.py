import cv2
import numpy as np

# Load the image
image = cv2.imread("/home/pinal-gadhiya/Downloads/Pinal-backup/Pinal Gadhiya/Digital_Signal & Image_Processing/Lab_Exp_9/linear_filt.jpeg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Define the size of the Averaging filter kernel
kernel_size = (5, 5)

# Create the Averaging filter kernel
kernel = np.ones(kernel_size, dtype=np.float32) / (kernel_size[0] * kernel_size[1])

# Apply the Averaging filter for smoothing
smoothed_image = cv2.filter2D(image, -1, kernel)

# Display the original and smoothed images
cv2.imshow("Original Image", image)
cv2.imshow("Smoothed Image - Averaging Filter", smoothed_image)

cv2.waitKey(0)
cv2.destroyAllWindows()