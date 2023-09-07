# rotate an image
import cv2 as cv

img = cv.imread('cat.jpg')

img = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)

cv.imshow('rotate', img)

cv.waitKey(0)