from cv2 import waitKey
import face_recognition as fr
import os
import cv2
import numpy as np



images = []
names = []
path = "faces"
for i in os.listdir(path):
    img = cv2.imread(os.path.join(path, i))
    images.append(img)
    names.append(os.path.splitext(i)[0])

def encoder(images):
    encode_list = []
    for img in images:
        encode = fr.face_encodings(img)[0]
        encode_list.append(encode)
    return encode_list


known = encoder(images)
print(len(known))

cap = cv2.VideoCapture(1)

while True:
    sucess,img = cap.read()
    imgS = cv2.resize(img, (0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    fl = fr.face_locations(imgS)
    ef = fr.face_encodings(imgS,fl)

    for encod,facl in zip(ef,fl):
        matches = fr.compare_faces(known,encod)
        dis = fr.face_distance(known,encod)
        matchIndex = np.argmin(dis)

        if matches[matchIndex]:
            name = names[matchIndex]
            print(name)
    cv2.imshow('Webcam',img)
    cv2,waitKey(1)



