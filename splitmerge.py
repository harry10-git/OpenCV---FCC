import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')
# cv.imshow('img', img)

blank = np.zeros(img.shape[:2], dtype ='uint8')

b,g,r = cv.split(img)


blue = cv.merge([b,blank,blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged_img = cv.merge([b,g,r])
cv.imshow('merged image', merged_img)

cv.waitKey(0)