# brightspot detection
import cv2 as cv

img = cv.imread('moon.jpeg')

img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

min, max, minloc, maxloc = cv.minMaxLoc(img)

circle = cv.circle(img, maxloc, 10, (0,255,0), 2)

cv.imshow('moon', circle)

cv.waitKey(0)