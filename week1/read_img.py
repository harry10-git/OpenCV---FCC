# read display and write an image
import cv2 as cv

img = cv.imread('cat.jpg')
cv.imshow('cat', img)

cv.imwrite('cat2.jpg', img)

cv.waitKey(0)