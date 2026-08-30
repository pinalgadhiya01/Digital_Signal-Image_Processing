import cv2
import numpy as np

# Load the image
image = cv2.imread("/home/pinal-gadhiya/Downloads/Pinal-backup/Pinal Gadhiya/Digital_Signal & Image_Processing/Lab_Exp_9/cube-1655118_640.webp")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Apply Gaussian smoothing to reduce noise
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Create a Laplacian kernel for sharpening
laplacian_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
], dtype=np.float32)

# Apply the Laplacian filter for sharpening
sharpened_image = cv2.filter2D(
    blurred_image, -1, laplacian_kernel
)

# Display the original, blurred, and sharpened images
cv2.imshow("Original Image", image)
cv2.imshow("Blurred Image", blurred_image)
cv2.imshow("Sharpened Image - High Pass Filter", sharpened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()