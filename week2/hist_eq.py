'''Histogram equalization is a method in image processing of contrast adjustment using the image’s histogram.
This method usually increases the global contrast of many images, especially when the usable data 
of the image is represented by close contrast values. Through this adjustment, the intensities can
be better distributed on the histogram. This allows for areas of lower local contrast to gain a higher
 contrast. Histogram equalization accomplishes this by effectively spreading out the most frequent
intensity values. The method is useful in images with backgrounds and foregrounds that are
 both bright or both dark.
''' 
import cv2 as cv
import numpy as np

img = cv.imread('demo.jpg',0)

equ = cv.equalizeHist(img)
res = np.hstack((img, equ))

cv.imshow('histogram equalization', res)

cv.waitKey(0)