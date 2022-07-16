from PIL import ImageGrab
import cv2
from cv2 import cvtColor
import numpy
from win32api import GetSystemMetrics
from pynput.keyboard import Key, Listener


frames = []
keys = []
key_presses = []
def on_press(key):
    if key not in key_presses:
        key_presses.append(key)

def on_release(key):
    if key in key_presses:
        key_presses.remove(key)
    if key == Key.esc:
        # Stop listener
        return False

from threading import Thread
def start_thread():
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

t1 = Thread(target=start_thread)
t1.start()
    
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
while True:
    img = ImageGrab.grab(bbox=(0,30,790,610))
    img = numpy.array(img)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img = cvtColor(img,cv2.COLOR_RGB2GRAY)
    frames.append(img)
    print(key_presses)
    keys.append(key_presses)
    cv2.imshow('Screen',img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
    

import pickle
with open("samples.json","wb") as f:
    frame_and_keys = []
    for i in range(len(frames)):
        frame_and_keys.append((frames[i],keys[i]))

    pickle.dump(frame_and_keys,file=f)
    print("Finished")


