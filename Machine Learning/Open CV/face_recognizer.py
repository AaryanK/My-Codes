import face_recognition
from face_recognition.api import face_locations
import numpy as np
import cv2
# import concurrent.futures
import os


    

import pickle
with open('faces.pickle', 'rb') as handle:
    faces = pickle.load(handle)





face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

capture = cv2.VideoCapture(0)


while True:
    _,frame = capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]
    # face_loc = face_recognition.face_locations(frame)[0]
    # encoded = face_recognition.face_encodings(frame)[0]
    # cv2.rectangle(frame,(face_loc[3],face_loc[0]),(face_loc[1],face_loc[2]),(255,0,0),2)
    # cv2.imshow("Aaryan",frame)
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            known_face_encodings = []
            known_face_names = [face for face in faces]
            for i in known_face_names:
                known_face_encodings.append(faces[i])
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            # face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            # best_match_index = np.argmin(face_distances)
            # if matches[best_match_index]:
            #     name = known_face_names[best_match_index]

            face_names.append(name)
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255,0), 2)

        # Draw a label with a name below the face
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    process_this_frame = not process_this_frame
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
