# extract rgb values of a pixel
import cv2 as cv

img = cv.imread('cats.jpg')
cv.imshow('cats', img)

# Extract RGB values of a specific pixel (e.g., pixel at coordinates (100, 100))
x, y = 100, 100
pixel_value = img[y, x]

print(pixel_value)

cv.waitKey(0)