import cv2
import numpy as np

# Load the image
image = cv2.imread('pic.jpeg')

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply median filter for noise reduction
filtered_image = cv2.medianBlur(gray_image, 5)

# Perform segmentation (simplified, you may need to adjust parameters)
_, segmented_mask = cv2.threshold(filtered_image, 200, 255, cv2.THRESH_BINARY)

# Apply morphological operations (closing) for refinement
kernel = np.ones((5, 5), np.uint8)
refined_mask = cv2.morphologyEx(segmented_mask, cv2.MORPH_CLOSE, kernel)

# Create a colored output image
output_image = np.zeros_like(image)
output_image[refined_mask == 255] = [0, 255, 0]  # Green for periphery
output_image[refined_mask == 0] = [255, 0, 0]   # Red for innermost core

# Display or save the segmented image
cv2.imshow('Segmented Image', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
