import os
import time
os.environ.__setitem__('DISPLAY', ':0.0')
import PySimpleGUI as sg
sg.change_look_and_feel('Dark')



bot = ['Hey Aaryan How can I help you? ']
me = []
bot_reply=['hello','hey']
layout = [[sg.Text("Dragon",key='Name',font=("Arial",15),text_color='white',background_color="Black",justification="center",size=(15,3))],
        [sg.Text("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ",key='19',font=("Arial",15),text_color='white',justification="left",background_color="Black")],
        [sg.Text("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ",key='18',font=("Arial",15),text_color='white',justification="left",background_color="Black")],
        [sg.Text("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ",key='17',font=("Arial",15),text_color='white',justification="right",background_color="Black")],
        [sg.Text("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ",key='16',font=("Arial",15),text_color='white',justification="left",background_color="Black")],
        [sg.Text("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ",key='15',font=("Arial",15),text_color='white',justification="right",background_color="Black")],
        [sg.Text("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ",key='14',font=("Arial",15),text_color='white',justification="left",background_color="Black")],
        [sg.Text("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ",key='13',font=("Arial",15),text_color='white',background_color="Black",justification="right")],
        [sg.Text("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ",key='12',font=("Arial",15),text_color='white',justification="left",background_color="Black")],
        [sg.Text("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ",key='11',font=("Arial",15),text_color='white',justification="right",background_color="Black")],
        [sg.Text("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ",key='10',font=("Arial",15),text_color='white',justification="left",background_color="Black")],
        [sg.Text("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ",key='9',font=("Arial",15),text_color='white',justification="right",background_color="Black")],
        [sg.Text("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ",key='8',font=("Arial",15),text_color='white',justification="left",background_color="Black")],
        [sg.Text("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ",key='7',font=("Arial",15),text_color='white',justification="right",background_color="Black")],
        [sg.Text("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ",key='6',font=("Arial",15),text_color='white',justification='right',background_color="Black")],
        [sg.Text("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ",key='5',font=("Arial",15),text_color='white',justification="right",background_color="Black")],
        [sg.Text("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ",key='4',font=("Arial",15),text_color='white',justification="left",background_color="Black")],
        [sg.Text("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ",key='3',font=("Arial",15),text_color='white',justification="right",background_color="Black")],
        [sg.Text("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ",key='2',font=("Arial",15),text_color='white',background_color="Black")],
        [sg.Text("Bot : Hey Aaryan How can I help you?                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ",key='1',font=("Arial",15),text_color='white',background_color="Black")],
        [sg.Text("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ",key='0',font=("Arial",15),text_color='white',background_color="Black")],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
        
        [sg.InputText(do_not_clear=False,size=(300,200),key="input")],
        [sg.Button("Send",key='Submit'),sg.Button("Exit",key='exit')]]

window = sg.Window(layout=layout,no_titlebar=True,title='Aaryan',background_color='black',size=(500,750),location=(900,0),resizable=True,grab_anywhere=True,keep_on_top=True)


while True:
    
    event,value = window.read()
    if event=='exit':
        quit()
    if event=="Submit" and value["input"] !='':
        me.append(value['input'])
        if len(me)==1:
            window['3'].update('Bot : '+bot[0])
            window['2'].update('Aaryan : '+me[0])
            window['1'].update('Bot : '+bot_reply[0])
        if len(me)==2:
            window['5'].update('Bot: '+bot[0])
            window['4'].update('Aaryan : '+me[0])
            window['3'].update('Bot : '+bot_reply[0])
            window['2'].update('Aaryan : '+me[1])
            window['1'].update('Bot : '+bot_reply[0])

        if len(me)==3:
            window['7'].update('Bot: '+bot[0])
            window['6'].update('Aaryan : '+me[0])
            window['5'].update('Bot : '+bot_reply[0])
            window['4'].update('Aaryan : '+me[1])
            window['3'].update('Bot : '+bot_reply[0])
            window['2'].update('Aaryan : '+me[2])
            window['1'].update('Bot : '+bot_reply[0])

        if len(me)==4:
            window['9'].update('Bot: '+bot[0])
            window['8'].update('Aaryan : '+me[0])
            window['7'].update('Bot : '+bot_reply[0])
            window['6'].update('Aaryan : '+me[1])
            window['5'].update('Bot : '+bot_reply[0])
            window['4'].update('Aaryan : '+me[2])
            window['3'].update('Bot : '+bot_reply[0])
            window['2'].update('Aaryan : '+me[3])
            window['1'].update('Bot : '+bot_reply[0])

        if len(me)==5:
            window['11'].update('Bot: '+bot[0])
            window['10'].update('Aaryan : '+me[0])
            window['9'].update('Bot : '+bot_reply[0])
            window['8'].update('Aaryan : '+me[1])
            window['7'].update('Bot : '+bot_reply[0])
            window['6'].update('Aaryan : '+me[2])
            window['5'].update('Bot : '+bot_reply[0])
            window['4'].update('Aaryan : '+me[3])
            window['3'].update('Bot : '+bot_reply[0])
            window['2'].update('Aaryan : '+me[4])
            window['1'].update('Bot : '+bot_reply[0])

        if len(me)==6:
            window['13'].update('Bot: '+bot[0])
            window['12'].update('Aaryan : '+me[0])
            window['11'].update('Bot : '+bot_reply[0])
            window['10'].update('Aaryan : '+me[1])
            window['9'].update('Bot : '+bot_reply[0])
            window['8'].update('Aaryan : '+me[2])
            window['7'].update('Bot : '+bot_reply[0])
            window['6'].update('Aaryan : '+me[3])
            window['5'].update('Bot : '+bot_reply[0])
            window['4'].update('Aaryan : '+me[4])
            window['3'].update('Bot : '+bot_reply[0])
            window['2'].update('Aaryan : '+me[5])
            window['1'].update('Bot : '+bot_reply[0])

        if len(me)==7:
            window['15'].update('Bot: '+bot[0])
            window['14'].update('Aaryan : '+me[0])
            window['13'].update('Bot : '+bot_reply[0])
            window['12'].update('Aaryan : '+me[1])
            window['11'].update('Bot : '+bot_reply[0])
            window['10'].update('Aaryan : '+me[2])
            window['9'].update('Bot : '+bot_reply[0])
            window['8'].update('Aaryan : '+me[3])
            window['7'].update('Bot : '+bot_reply[0])
            window['6'].update('Aaryan : '+me[4])
            window['5'].update('Bot : '+bot_reply[0])
            window['4'].update('Aaryan : '+me[5])
            window['3'].update('Bot : '+bot_reply[0])
            window['2'].update('Aaryan : '+me[6])
            window['1'].update('Bot : '+bot_reply[0])
        
        if len(me)==8:
            window['17'].update('Bot: '+bot[0])
            window['16'].update('Aaryan : '+me[0])
            window['15'].update('Bot : '+bot_reply[0])
            window['14'].update('Aaryan : '+me[1])
            window['13'].update('Bot : '+bot_reply[0])
            window['12'].update('Aaryan : '+me[2])
            window['11'].update('Bot : '+bot_reply[0])
            window['10'].update('Aaryan : '+me[3])
            window['9'].update('Bot : '+bot_reply[0])
            window['8'].update('Aaryan : '+me[4])
            window['7'].update('Bot : '+bot_reply[0])
            window['6'].update('Aaryan : '+me[5])
            window['5'].update('Bot : '+bot_reply[0])
            window['4'].update('Aaryan : '+me[6])
            window['3'].update('Bot : '+bot_reply[0])
            window['2'].update('Aaryan : '+me[7])
            window['1'].update('Bot : '+bot_reply[0])

        if len(me)==9:
            window['19'].update('Bot: '+bot[0])
            window['18'].update('Aaryan : '+me[0])
            window['17'].update('Bot : '+bot_reply[0])
            window['16'].update('Aaryan : '+me[1])
            window['15'].update('Bot : '+bot_reply[0])
            window['14'].update('Aaryan : '+me[2])
            window['13'].update('Bot : '+bot_reply[0])
            window['12'].update('Aaryan : '+me[3])
            window['11'].update('Bot : '+bot_reply[0])
            window['10'].update('Aaryan : '+me[4])
            window['9'].update('Bot : '+bot_reply[0])
            window['8'].update('Aaryan : '+me[5])
            window['7'].update('Bot : '+bot_reply[0])
            window['6'].update('Aaryan : '+me[6])
            window['5'].update('Bot : '+bot_reply[0])
            window['4'].update('Aaryan : '+me[7])
            window['3'].update('Bot : '+bot_reply[0])
            window['2'].update('Aaryan : '+me[8])
            window['1'].update('Bot : '+bot_reply[0])
            



        '''try:
            window['ME3'].update(window['ME2'])
            window['ME4'].update(window['ME3'])
            window['ME5'].update(window['ME4'])
            window['ME6'].update(window['ME5'])
            window['ME7'].update(window['ME6'])
            window['ME8'].update(window['ME7'])
            window['ME9'].update(window['ME8'])
            window['ME10'].update(window['ME9'])

        except:
            pass
    '''
