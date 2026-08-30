import cv2
import numpy as np

# Load the image
image = cv2.imread('/home/pinal-gadhiya/Downloads/Pinal-backup/Pinal Gadhiya/Digital_Signal & Image_Processing/Lab_Exp_9/duck.jpg')

# Define the Gaussian kernel for smoothing
kernel_size = (5, 5)
sigma = 1.5

gaussian_kernel = cv2.getGaussianKernel(kernel_size[0], sigma)
gaussian_kernel = np.outer(gaussian_kernel, gaussian_kernel)

# Apply Gaussian smoothing
smoothed_image = cv2.filter2D(image, -1, gaussian_kernel)

# Define a sharpening kernel
sharpening_kernel = np.array([
    [-1, -1, -1],
    [-1,  9, -1],
    [-1, -1, -1]
])

# Apply sharpening
sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)

# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("Gaussian Smoothed Image", smoothed_image)
cv2.imshow("Sharpened Image", sharpened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()