import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('img', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)


# Sobel
sobelX = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobelY = cv.Sobel(gray, cv.CV_64F, 0, 1)

combined_sobel = cv.bitwise_or(sobelX, sobelY)

#cv.imshow('sobel X', sobelX)
#cv.imshow('sobel Y', sobelY)
cv.imshow('combined sobel', combined_sobel)

# Canny
canny = cv.Canny(gray, 150, 175)
cv.imshow('canny', canny)

cv.waitKey(0)