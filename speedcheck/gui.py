import os
from checker import check

os.environ.__setitem__('DISPLAY', ':0.0')

import PySimpleGUI as sg
import concurrent.futures
sg.ChangeLookAndFeel('Black')
layout = [[sg.Text('This Will Take a Moment',key='Upload')],
        [sg.Text('',key='Download')]]

window = sg.Window('Network View', layout, no_titlebar=True,location=(150,0),size=(300,35),grab_anywhere=True,keep_on_top=True)

def w():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        value =executor.submit(check)
        while True:
            events,values = window.read()
            window['Upload'].update('Upload speed : ', u ,'Mbps')
            window['Download'].update('Download speed : ', d ,'Mbps')    
        

w()

    