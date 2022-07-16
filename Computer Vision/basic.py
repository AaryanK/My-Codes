import cv2 as cv

def resize(frame,scale):
    scale=(scale/100)
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

img = resize(cv.imread('images/cat1.jpg'),25)

cv.imshow('Cat',img)


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Grayed',gray)

blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

canny = cv.Canny(img,125,175)
cv.imshow('Canny',canny) 

cv.waitKey(0)