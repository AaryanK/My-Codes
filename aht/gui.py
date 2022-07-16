import os
import time
os.environ.__setitem__('DISPLAY', ':0.0')

import PySimpleGUI as sg
sg.theme('DarkPurple6')




def popupmessage(messagetodisplay,character=None,bgcolour=None,texttoshow=None,time=None):
    result = sg.popup_get_text(message=messagetodisplay,password_char=character,default_text=texttoshow,title='AHT')
    return result  

def major(layout):
    layout = [[sg.Button('Send',key='clicked')]]
    window = sg.Window(layout=layout,size=(60,30),no_titlebar=True,title='AHT',location=(570,0),keep_on_top=True,grab_anywhere=False)
    while True:
        event,value = window.read()
        if event == 'clicked':
            return 'clicked'

    
