import PySimpleGUI as sg
import bs4
import requests
from PIL import Image
import random
import io
def get_data():
    
    country_data = []
    response = requests.get('https://www.worldatlas.com/countries')
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    countries = soup.find(id='country_list')
    #print(countries.find_all('li'))
    c = 0
    for li in countries.find_all('li'):
        country_list= []
        c += 1
        flag_link = li.find('img').get('src')
        country_name = li.h3.get_text()
        capital = li.table.find_all('tr')[3].td.get_text()
        #print(capital)
        country_list.append(country_name)
        country_list.append(flag_link)
        country_list.append(capital)
        cunt = country_list
        country_data.append(cunt)
        
    return country_data

countries_data = get_data()

import random

country = countries_data
sg.theme('DarkTeal1')
result = ""


random_picker = random.randint(0, len(country) -1 )
    #print(random_picker)
d_country = country[random_picker][0]
    #print(d_country)
d_capital = country[random_picker][2]

layout = [

    [sg.Text("hola")],
    [sg.Text(f"{d_country}",key="country")],
    [sg.Text(f"CAPITAL IS ? "), sg.InputText()],
    [sg.Button("enter"), sg.Button("next")],
    [sg.Text(size=(12,1), key='-OUTPUT-')],
    [sg.Text("the answer is : "),sg.Text(size=(12,1), key='-ruh-')]
   

    ]

    
window = sg.Window("hello world", layout, size =(1000,600))



while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "enter":
        if (values[0]).upper() == (d_capital).upper():
            result = "correct"
            random_picker = random.randint(0, len(country) -1 )
            #print(random_picker)
            d_country = country[random_picker][0]
            window['country'].update(d_country)
            d_capital = country[random_picker][2]
            
        else:
            result = "wrong kys"
            answer = d_capital
            window["-ruh-"].update(answer)
        
    

        window['-OUTPUT-'].update(result)

    

window.close()