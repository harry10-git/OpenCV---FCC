import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')

# translate
def tranlate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = tranlate(img, 100, 50)
cv.imshow('translated', translated)

# rotate
def rotate(img, angle, rotPoint= None):
    (height, width) = img.shape[:2] # get first 2 values
    if rotPoint is None:
        rotPoint = (width//2, height//2)

    dimensions = (width, height)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, scale=1.0)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 60) # rotate anti-clockwise
cv.imshow('rotated', rotated)

# resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('resized', resized)

# flip an image
flipped = cv.flip(img, flipCode=1) # 0 for vertical flip, 1 for horizontal flip, -1 for both
cv.imshow('flipped', flipped)

# cropping
cropped = img[200:400, 300:500]
cv.imshow('cropped', cropped)


cv.waitKey(0)

