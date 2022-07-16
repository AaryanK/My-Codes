import os 
os.environ['DISPLAY'] = ':0'
import pyautogui as pg
import time

time.sleep(5)

print(pg.position())