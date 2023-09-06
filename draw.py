import cv2 as cv
import numpy as np

blank = np.zeros((500,500, 3), dtype='uint8') # height , width and number of color channels
cv.imshow('blank', blank)

# 1. 200 to 300 and 300 to 400
'''blank[200:300, 300:400] =  0, 0, 255 # set to Red - BGR
cv.imshow('Red', blank)'''

# 2. Draw a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness= cv.FILLED) # img, start, end, bgr, thickness
cv.imshow('Rectangle', blank)

# 3. Draw a circle
cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness= -1)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness= 2) # white line
cv.imshow('Circle', blank)

# 5. Write Text
cv.putText(blank, 'Hello World', (0,300), cv.FONT_HERSHEY_COMPLEX, 1.0, (255,0,0), 1)
cv.imshow('Text', blank)

cv.waitKey(0)
