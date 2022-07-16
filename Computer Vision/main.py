import cv2 as cv


def rescale(frame,scale=0.2):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

img = cv.imread('images/cat1.jpg')

cv.imshow('Cat',img)

capture = cv.VideoCapture('videos/video1.mp4')

while True:
    isTrue,frame = capture.read()
    frameResized = rescale(frame)
    cv.imshow('Video',frame)
    cv.imshow('Resized',frameResized)


    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()






cv.waitKey(0)