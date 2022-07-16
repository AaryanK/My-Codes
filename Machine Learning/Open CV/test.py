import face_recognition 
import cv2
import json
import os

faces = {}


image = face_recognition.load_image_file("faces/Aaryan.png")
encodings = face_recognition.face_encodings(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
for files in os.listdir('faces'):
    image = face_recognition.load_image_file(f"faces/{files}")
    encodings = face_recognition.face_encodings(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
    faces[f"{files.split('.jpg')[0]}"] = encodings[0]

print(faces)

import pickle
with open('faces.pickle', 'wb') as handle:
    pickle.dump(faces, handle)