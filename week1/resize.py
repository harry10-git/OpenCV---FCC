# resize an image
import cv2 as cv

img = cv.imread('cats.jpg')
img2 = cv.resize(img, (500,500), interpolation= cv.INTER_AREA)
cv.imshow('resized', img2)


cv.waitKey(0)