import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
# cv.imshow('circle', circle)
masked = cv.bitwise_and(img,img, mask= mask)
cv.imshow('masked', masked)

# Grayscale histogram
# gray_hist = cv.calcHist([img], [0], mask, [256], [0,256]) # mask - histogram of a circle mask

# plt.figure()
# plt.title('GrayScale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# Color Histogram

plt.figure()
plt.title('Colored Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

colors = ('b', 'g', 'r')
for i,col in enumerate(colors):  # enumerate gives indexing
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color = col)
    plt.xlim([0, 256])

plt.show()

cv.waitKey(0)