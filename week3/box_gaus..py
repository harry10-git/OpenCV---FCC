import cv2 as cv
import numpy as np


def apply_box_filter(image):
    box_filtered = cv.boxFilter(image, -1, (5, 5))
    return box_filtered


def apply_gaussian_filter(image):
    gaussian_filtered = cv.GaussianBlur(image, (5, 5), 0)
    return gaussian_filtered

img = cv.imread('cats.jpg')
box_filter = apply_box_filter(img)
gaus_filer = apply_gaussian_filter(img)


res = np.hstack((box_filter, gaus_filer))
cv.imshow('Box vs Gaussian', res)

cv.waitKey(0)