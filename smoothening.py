import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')

# Average blur
blur = cv.blur(img, (3,3))
cv.imshow('Average blur', blur)

# Gaussian Blur
gaussian = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gaussian)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral Blur (blurs images but retains edges)
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("Bilateral Blur", bilateral)


cv.waitKey(0)