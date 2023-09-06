import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')

blank = np.zeros(img.shape, dtype= 'uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# blur
# blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
# canny 
# canny = cv.Canny(blur, 125, 175)
#cv.imshow('canny', canny)

ret , thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)



contours, heirarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} are present!!')

cv.drawContours(blank, contours, -1, (0,0,255), thickness=1)
cv.imshow('blank', blank)

cv.waitKey(0)