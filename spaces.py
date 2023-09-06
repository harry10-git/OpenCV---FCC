import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/park.jpg')
#cv.imshow('park', img)

# gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# hsv
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)
          
# hsv to bgr
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv -> bgr', hsv_bgr)

cv.waitKey(0)