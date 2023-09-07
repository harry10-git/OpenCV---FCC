import cv2 as cv
import numpy as np

def calc_gradient(img_path):
    img = cv.imread(img_path, 0)

    # Calculate gradient in both X and Y directions using Sobel operators
    gradient_x = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)
    gradient_y = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=3)

    # Calculate magnitude and orientation of the gradient
    gradient_magnitude = np.sqrt(gradient_x ** 2 + gradient_y ** 2)
    gradient_orientation = np.arctan2(gradient_y, gradient_x) * (180 / np.pi)

    return gradient_magnitude, gradient_orientation

img_path = 'cats.jpg'

grad_mag, grad_angle = calc_gradient(img_path)

cv.imshow("Original Image", cv.imread(img_path))
cv.imshow("Gradient Magnitude", grad_mag.astype(np.uint8))

cv.waitKey(0)