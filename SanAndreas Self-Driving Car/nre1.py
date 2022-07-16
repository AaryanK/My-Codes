import pickle
import cv2

with open("samples.json",'rb') as f:
    json = pickle.load(f)

for i in json:
    print(i[1])
    cv2.imshow('Setup',i[0]) 
    cv2.waitKey(1)