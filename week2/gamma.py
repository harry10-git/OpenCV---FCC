'''Gamma correction is important for displaying images on a screen correctly, to prevent bleaching 
or darkening of images when viewed from different types of monitors with different display settings.
This is done because our eyes perceive images in a gamma-shaped curve, whereas cameras capture images
in a linear fashion. '''

import cv2 as cv
import numpy as np

img = cv.imread('demo.jpg')

for gamma in [0.1, 0.5, 1.2, 2.2]:
    gamma_corrected = np.array(255* (img/255)**gamma, dtype='uint8')

    cv.imshow('gamma_'+str(gamma), gamma_corrected)

cv.waitKey(0)