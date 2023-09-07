import cv2 as cv

img = cv.imread('cats.jpg')

blur = cv.GaussianBlur(img, (5,5), 0)

canny = cv.Canny(blur, 75, 150, cv.THRESH_BINARY)

cv.imshow('canny', canny)

cv.waitKey(0)