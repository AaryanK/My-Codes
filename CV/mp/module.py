import cv2
import mediapipe as mp
import numpy as np

def give_landmarks(results):
    arr = np.zeros(shape=(21,2))
    for hm in results.multi_hand_landmarks:
        print(enumerate(hm.landmark))
        # for idnumber,lm in enumerate(hm.landmark):
        #     print(idnumber)
        #     h,w,c = 480, 640, 3
        #     cx,cy = int(lm.x*w),int(lm.y*h)
        #     arr[idnumber,0],arr[idnumber,1] = cx,cy

        #     return arr

            
