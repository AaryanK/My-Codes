import cv2
import numpy as np
import PIL
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For webcam input:
cap = cv2.VideoCapture(1)
count = 0
while cap.isOpened():
  success, image = cap.read()
  gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  for (x,y,w,h) in faces:
    print(x,y,w,h)
    cv2.circle(image,(x,y),10,(255,0,0),-1)
    cv2.circle(image,(x+w,y),10,(255,0,0),-1)
    cv2.circle(image,(x+w,y+h),10,(255,0,0),-1)
    cv2.circle(image,(x,y+h),10,(255,0,0),-1)
    img = cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
    img = gray[y:y+h,x:x+w]
    if count <1000:
      cv2.imwrite("train/face_"+str(count)+".jpg",img)
      count+=1
    cv2.imshow('MediaPipe Hands', img)
  if cv2.waitKey(5) & 0xFF == 27:
    break
cap.release()