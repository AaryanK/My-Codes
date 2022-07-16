import cv2 as cv





capture = cv.VideoCapture(0)

while True:
    isTrue,frame = capture.read()
    frameResized = cv.Canny(frame,100,175)
    cv.rectangle(frame,(474,104),(611,348),(255,0,0),2)
    cv.imshow('Video',frame)
    cv.imshow('Resized',frameResized)


    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()