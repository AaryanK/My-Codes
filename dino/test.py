import os
import pyscreenshot as ImageGrab
from PIL import Image
import pyautogui 
import time

def hit(key):
    pyautogui.press(key)
    return

def isCollide(data):
    '''for i in range (260,495):
        for j in range(600,650):
            if data[i,j] > 150:'''
    
    '''for i in range(260,495):
        for j in range(345,410):
            if data[i, j] < 85:
                print('I see maybe a bird ,I guess I should duck')
                hit("down")
                return'''

    for i in range(395,405):
        for j in range(315,340):
            if data[i, j] < 100:
                print('I see a cactus ,I guess I should jump')
                hit('up')
                return 
            '''elif data[i,j]<100:
                for i in range(260,495):
                    for j in range(345,410):
                        if data[i, j] < 215:
                            print('I see maybe a bird ,I guess I should duck')
                            hit("down")
                            return

                for i in range(260,495):
                    for j in range(415,510):
                        if data[i, j] > 200:
                            print('I see a cactus ,I guess I should jump')
                            hit('up')
                            return '''
    return

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    hit('up') 

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        
        isCollide(data)
            
        