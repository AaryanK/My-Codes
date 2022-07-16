import cv2 
import mediapipe as mp
import time

from module import give_landmarks
cap = cv2.VideoCapture(1)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
drawer = mp.solutions.drawing_utils

start_time = 0 
current_time = 0

while True:
    success,frame = cap.read()
    RGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    # print(RGB.shape)
    results = hands.process(RGB)
    if results.multi_hand_landmarks:
            lm = give_landmarks(results)
            # print(lm)
            # cv2.circle(RGB,(lm[4,0],lm[4,1]),25,(255,0,255),cv2.FILLED)
            # cv2.circle(RGB,(lm[4,8],lm[4,1]),25,(255,0,255),cv2.FILLED)
            # drawer.draw_landmarks(RGB,hm,mp_hands.HAND_CONNECTIONS)
    cv2.imshow("Image",RGB)

    cv2.waitKey(1)