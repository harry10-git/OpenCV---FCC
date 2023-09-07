import cv2 as cv

img = cv.imread('demo.jpg')
cv.imshow('normal', img)

resize_img = cv.resize(img, [200,200])
cv.imshow('resize', resize_img)

cropped_img = img[100:200, 200: 350]
cv.imshow('croped', cropped_img)

cv.waitKey(0)