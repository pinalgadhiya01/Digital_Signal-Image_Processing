import cv2
import numpy as np

# 1. Load the image in grayscale
image = cv2.imread('/home/pinal-gadhiya/Downloads/Pinal-backup/Pinal Gadhiya/Digital_Signal & Image_Processing/Lab_Exp_12/image3.png', 0)

# Check whether image is loaded successfully
if image is None:
    print("Error: Image not found. Check the image path.")
    exit()

# 2. Convert grayscale image into binary image
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# 3. Define the structuring element
pattern = np.array([
    [-1,  1, -1],
    [ 1,  1,  1],
    [-1,  1, -1]
], dtype=np.int8)

# 4. Apply Hit-or-Miss Transformation
result = cv2.morphologyEx(binary, cv2.MORPH_HITMISS, pattern)

# 5. Display the original and result images
cv2.imshow('Original Image', image)

cv2.imshow('Binary Image', binary)

cv2.imshow('Hit-or-Miss Transformation', result)

# 6. Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
