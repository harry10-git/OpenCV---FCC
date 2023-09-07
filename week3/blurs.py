# different types of blurring
import cv2 as cv

img = cv.imread('cats.jpg')
cv.imshow('normal', img)

# Gaussian Blur
gaus = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('gaussian', gaus)

# Median Blur
median = cv.medianBlur(img, 7)
cv.imshow('median', median)

# Bilateral blur
bilat = cv.bilateralFilter(img, 9, 75, 75)
cv.imshow('bilateral', bilat)


cv.waitKey(0)