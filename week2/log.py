'''Logarithmic transformation of an image is one of the gray level image transformations. 
Log transformation of an image means replacing all pixel values, present in the image,
with its logarithmic values. Log transformation is used for image enhancement as 
it expands dark pixels of the image as compared to higher pixel values.'''

import cv2 as cv
import numpy as np

img = cv.imread('grayscale2.jpg')

c = 255/ np.log(1 + np.max(img))
log_img = c * (np.log(img+1))

# convert to uint8
log_img = np.array(log_img, dtype = np.uint8)
cv.imshow('log transform', log_img)

cv.waitKey(0)