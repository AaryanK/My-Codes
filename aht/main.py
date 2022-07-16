from gui import popupmessage,major
from engine import sendEmail,twilio_send_msg,give_message
from cpu import make_processes,make_thread,execute
import os
# os.environ.__setitem__('DISPLAY', ':0.0')
import PySimpleGUI as sg
# os.environ['DISPLAY'] = ':0'
import pyautogui
from notification import notify
# os.environ.__setitem__('XDG_SESSION_TYPE','wayland')
import clipboard

layout = [[sg.Button('Send',key='clicked')]]

result = execute(major,args=(layout))
if result == 'clicked':
    notify('Your pc will be automated now')
    pyautogui.moveTo(500,500)
    pyautogui.hotkey('ctrl','a')
    pyautogui.hotkey('ctrl','c')
    rawdata = clipboard.paste()
    file = open('rawdata.txt','w')
    file.write(rawdata)
    file.close()
    email = execute(popupmessage,args=('Enter client\'s mail'))
    phone=  execute(popupmessage,args=('Enter client\'s phone'))
    try:
        sendEmail(email)
        notify('Sent email success fully')
    except:
        notify('Maybethe mail was not sent')
    try:
        twilio_send_msg(phone,give_message())
        notify(f'Message sent to {phone}')
    except Exception as e:
        print(e)
        notify('Message not sent')