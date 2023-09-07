import cv2
import numpy as np

# Load an image
image = cv2.imread('lenna.jpg')

# Reshape the image to a 2D array of pixels (rows x columns, 3 channels)
pixels = image.reshape((-1, 3))

# Define the number of clusters (k)
k = 3

# Define criteria and apply k-means
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
_, labels, centers = cv2.kmeans(pixels.astype(np.float32), k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Convert the centers to integer values (RGB)
centers = np.uint8(centers)

# Map each pixel to the corresponding cluster center
segmented_image = centers[labels.flatten()]

# Reshape the segmented image back to its original shape
segmented_image = segmented_image.reshape(image.shape)

# Display the original and segmented images
cv2.imshow('Original Image', image)
cv2.imshow('Segmented Image', segmented_image)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
