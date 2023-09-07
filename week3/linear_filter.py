import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def linear_filter(img, kernel):
    k_height, k_width = kernel.shape
    img_height, img_width = img.shape[:2]

    pad_height = k_height//2
    pad_width = k_width//2

    padded_img = np.pad(img, ((pad_height, pad_height), (pad_width, pad_width),(0,0)), mode='constant')

    filter_img = np.zeros_like(img)

    for i in range(img_height):
        for j in range (img_width):
            patch = padded_img[i:i+k_height, j:j+k_width]
            filter_img[i,j] = np.sum((patch * kernel)// 9)
    
    return filter_img

img = cv.imread('cats.jpg')

kernel = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]])

filtered_image = linear_filter(img, kernel)

plt.figure(figsize= (10,5))
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(filtered_image)
plt.title('Filtered Image')

plt.tight_layout()
plt.show()




