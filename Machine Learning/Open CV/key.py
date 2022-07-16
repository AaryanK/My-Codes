import cv2
from cvzone.HandTrackingModule import HandDetector
cap = cv2.VideoCapture(0)
# cap.set(3,1280)
# cap.set(3,720)

detector = HandDetector(detectionCon=0.8)

def give_locations(img,key,row_number=1,key_number=1):
    x1,y1=40*key_number+previous_index[0],50*row_number
    # x2,y2=150*key_number,150*row_number
    cv2.rectangle(img,(x1,y1),(x1+50,y1+50),(52, 67, 235), cv2.FILLED)
    cv2.putText(img, key.upper(), (x1+13, y1+35), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
while True:
    success,img = cap.read()
    cv2.flip(img,1)
    hands,img = detector.findHands(img,flipType=True)
    # row1 = list("qwertyuiop")
    # row2=list("asdfghjkl;\'")
    # row3=list('zxcvbnm,./')


    # for i in row1:
    #     # print(i)
    #     j=1
    #     previous_index=[0,0]
    #     k_number=row1.index(i)+1
    #     give_locations(img,key=i,key_number=k_number,row_number=j)

    #     # previous_index[0] += 10

    # for i in row2:
    #     j=2
    #     # print(i)
    #     previous_index=[0,0]
    #     k_number=row2.index(i)+1
    #     give_locations(img,key=i,key_number=k_number,row_number=j)

    #     # previous_index[0] += 10

    # for i in row3:
    #     j=3
    #     # print(i)
    #     previous_index=[0,0]
    #     k_number=row3.index(i)+1
    #     give_locations(img,key=i,key_number=k_number,row_number=j)

        # previous_index[0] += 10



    cv2.imshow("Image",img)
    cv2.waitKey(1)

