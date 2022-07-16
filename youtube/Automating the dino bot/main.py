import pyscreenshot as ImageGrab 
#Use from PIL import ImageGrab if youre not getting error while using it!!
from PIL import Image
import pyautogui as pg
import time




def press(key):
    pg.press(key)

def touch(data,x1,x2,y1,y2):
    for i in range(x1,x2):
        for j in range(y1,y2):
            if data[i, j] >10:
                press('up')


while True:
    ss = ImageGrab.grab().convert('L')
    image_data = ss.load()
    touch(image_data,195,255,450,490)