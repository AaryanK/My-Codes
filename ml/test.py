import get_passwords
import PySimpleGUI as sg


'''sg.ChangeLookAndFeel('Black')
layout =[[sg.Text('plz enter your master password',key='header',font=('Digital-7',25),justification='center')],
        [sg.InputText(key='p',password_char='0',size=(60,60))],
        [sg.Button('submit',font=('Helvetica',25))]
        ]

window =sg.Window('passwords',layout,size =(500,500))

while True:
    event, values = window.read()
    if event ==('submit') and values['p']=='aarya123':
        window['header'].update('success')
        
    elif event ==('submit') and values['p']!='aarya123':
        window['header'].update('wrong pasword')

window.close()'''


        

def passwords():
    sg.ChangeLookAndFeel('Black')
    b =[[sg.Text('Passwords',key='header',justification='right',font=('Digital-7',25))]]
    sites = get_passwords.getpasswordsandusername()[0]
    for i in range(len(sites)):
        b.append([sg.Button(sites[i],font=('Helvetica',15))])
        b.append([sg.Text('',size=(15,10),key=sites[i]+'text',font=('Digital-7',25))])
        b.append([])

    window =sg.Window('passwords',b,size =(800,800))
    while True:
        event, values = window.read()
        if event in sites:
            window[sites[sites.index(event)]+'text'].update('success')
    window.close()
passwords()