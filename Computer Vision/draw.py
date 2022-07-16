import cv2 as cv
import numpy as np

def resize(frame,scale):
    scale=(scale/100)
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

blank = np.zeros((500,500,3),dtype='uint8')

cv.imshow('Blank',blank)
cv.rectangle(blank,(0,255),(150,500),(0,255,0),cv.FILLED)
cv.imshow('Green',blank)
cv.circle(blank,(250,250),40,(0,0,255),-1)
cv.imshow('Blue',blank)
cv.putText(blank,"Hello Open CV",(0,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow('Text',blank)

cv.waitKey(0)