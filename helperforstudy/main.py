from tkinter.scrolledtext import ScrolledText
import clipboard
import pyautogui
import PySimpleGUI as sg
import concurrent.futures
from sense import speak
from assist import give_meaning

def speak_selected():
    pyautogui.hotkey('ctrl','c')
    text = clipboard.paste()
    speak(text)

def execute(func,args=None):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        f1=executor.submit(func,args)
        return f1.result()

def major(layout):
    sg.theme('DarkPurple6')
    layout = [[sg.Button('speak',key='spk')],
                [sg.Button('mean',key='mean')],
                [sg.Button('close',key='close')]]
    window = sg.Window(layout=layout,title='Dragon',size=(80,140),location=(0,700),keep_on_top=True,grab_anywhere=True,no_titlebar=True)
    while True:
        event,value = window.read()
        if event == 'spk':
            return "speak"
        if event == "mean":
            return "mean"
        if event =="close" or event ==sg.WIN_CLOSED:
            return "close"
            break

def meaning():
    pyautogui.hotkey('ctrl','c')
    t = clipboard.paste()
    sg.theme('DarkPurple6')
    meaning = give_meaning(t)
    layout = [[sg.Multiline(meaning,autoscroll=True,size=(65,40),font=('Helvetica', 20),text_color="blue")],
            [sg.Button('speak',key='speak'),sg.Button('ok',key='okay')]]
    window = sg.Window(layout=layout,title=f"meaning of {t}",size=(600,340))
    while True:
        event,value = window.read()
        if event == "speak":
            speak(meaning)
        if event =="okay" or event ==sg.WIN_CLOSED:
            break

def main():
    while True:
        task = execute(major)
        if task =="close":
            break
        if task == "mean":
            meaning()
        if task == 'speak':
            speak_selected()
main()