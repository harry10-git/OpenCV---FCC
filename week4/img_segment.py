import cv2
import numpy as np
image = cv2.imread('park.jpg')

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_color = np.array([20, 100, 100])
upper_color = np.array([255, 255, 255])
color_mask = cv2.inRange(hsv_image, lower_color, upper_color)

segmented_image = cv2.bitwise_and(image, image, mask=color_mask)

cv2.imshow('Original Image', image)
cv2.imshow('Segmented Image', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()