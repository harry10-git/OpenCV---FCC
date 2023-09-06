import cv2 as cv

capture = cv.VideoCapture('Resources/Videos/dog.mp4')

def rescale(frame, scale = 0.75):
    # works for images , videos and live video
    width = int(frame.shape[1] * scale) # widht is 0th index
    height = int(frame.shape[0] * scale) # height is 1st index

    dimensions = (width, height)

    return cv.resize(frame, dimensions , interpolation= cv.INTER_AREA)

while True:
    isTrue , frame = capture.read()

    frame_resized = rescale(frame, scale = 0.2) # use created function to rescale

    cv.imshow('video' , frame)
    cv.imshow('video rescaled', frame_resized)

    if cv.waitKey(0) & 0xFf == ord('d'):
        break

capture.release()
cv.destroyAllWindows()


# chage res of Live video
'''def changeRes(height, width):
    capture.set(3, width)
    capture.set(4, height)'''
