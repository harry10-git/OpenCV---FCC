'''These functions, as the name suggests, are not entirely linear in nature.
However, they are linear between certain x-intervals. One of the most commonly used 
piecewise-linear transformation functions is contrast stretching.
This process expands the range of intensity levels in an image so that it spans the full 
intensity of the camera/display.'''

import cv2 as cv
import numpy as np

img = cv.imread('demo.jpg')

def pixelVal(pix, r1, s1, r2,s2):
    if(0<=pix and pix <= r1):
        return (s1/r1)*pix
    elif(r1< pix and pix<=r2):
        return ((s2-s1)/ (r2-r1)) * (pix - r1) + s1
    else:
        return ((255 - s2)/(255 - r2)) * (pix - r2) + s2

r1 = 70
s1 = 0
r2 = 140
s2 = 255

# Vectorize the function to apply it to each value in the Numpy array.
pixelVal_vec = np.vectorize(pixelVal)

contrast_stretched = pixelVal_vec(img, r1, s1, r2, s2)

cv.imshow('contrast stretchend', contrast_stretched)

cv.waitKey(0)