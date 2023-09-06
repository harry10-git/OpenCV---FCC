import cv2 as cv

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('park', img)

# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Blur - Gaussian Blur
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

# Edge cascade
canny = cv.Canny(blur, 125, 175) # pass blur image to detect fewer edges
cv.imshow('canny', canny)

# dilate the image
dilated = cv.dilate(canny, (3,3), iterations=3)  # use canny 
cv.imshow('dilated', dilated)

# erode
eroded = cv.erode(dilated,(3,3), iterations=3 ) # convert from dilated to canny
cv.imshow('erored', eroded)

# resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

# cropped
cropped = img[200:300, 200:500]
cv.imshow('Cropped', cropped)

cv.waitKey(0)