import discord
import time
import asyncio
# import main
import subprocess
import os
os.environ['DISPLAY'] = ':0'
import pyautogui as pg
import datetime

def attend(subject,name):

    subprocess.Popen(['/usr/bin/firefox',links[subject]])

    time.sleep(5)


    pg.click('name.png')

    pg.typewrite(name)

    pg.click(860, 441)

    time.sleep(10)

    pg.click('join.png')

    return 'joined'

    pg.moveTo(1084,1057)
    pg.click()
    pg.click(1672,1029)
    pg.typewrite('good morning')

    


def wait(subject,name):
    
    today=datetime.datetime.now().strftime('%A').lower()
    if subject in routine[today]:
        x = routine[today[subject]]
        while True: 
            for days in routine:
                if days==today:
                    for hours in days:
                        if subject == datetime.datetime.now().strftime('%H')+':'+datetime.datetime.now().strftime('%M'):
                            break

        attend(subject,name)          

token = 'NzI0ODE4ODU4NDI2NDk5MDcy.XvFuKg.ABJ4PeLleu9Nkgp4h3YifQ_fFtw'


links = {'maths':'https://us04web.zoom.us/wc/join/9562206942?wpk=wcpk45d618b025feeb5d287e59eaeffc2cbe',
         'nepali':'https://us04web.zoom.us/wc/join/2478253136?wpk=wcpk5fae43e84d911349e8a6548c7c271137',
         'science':'https://us04web.zoom.us/wc/join/8840743766?wpk=wcpk25255fda25c709e4e713092131000775',
         'eph':'https://us04web.zoom.us/wc/join/4639696441?wpk=wcpk56405c4e9414ba882517e244b9f6fee2',
         'social':'https://us04web.zoom.us/wc/join/8532062482?wpk=wcpk1a6512969006e4ce5a86503e10aa62c9',
         'computer':'https://us04web.zoom.us/wc/join/4563530400',
         'omaths':'https://us04web.zoom.us/wc/join/4413257070?wpk=wcpkf4e48ca54269451100f06f7eba16f7df'    
         }


routine = {'sunday':{'09:00':'nepali',
                    '09:50':'science',
                    '11:00':'maths',
                    '11:50':'computer'},

            'monday':{'09:00':'nepali',
                    '09:50':'science',
                    '11:00':'maths',
                    '11:50':'computer'},

            'tuesday':{'09:00':'nepali',
                    '09:50':'science',
                    '11:00':'maths',
                    '11:50':'computer'},

            'wednesday':{'09:00':'eph',
                    '09:50':'omaths',
                    '11:00':'social'},
            
            'thursday':{'09:00':'eph',
                    '09:50':'omaths',
                    '11:00':'social'},
                    
            'friday':{'09:00':'eph',
                    '09:50':'omaths',
                    '11:00':'social'}        
                    
            }


client = discord.Client()



@client.event


async def on_message(message):
    if message.channel.type is discord.ChannelType.private:
        uneligible = ['Assistant😎#6148']
        if str(message.author) not in uneligible:
            if '!join' in message.content:
                text=message.content.split()
                subject=text[1]
                subject=text[1]
                name=text[2]
                wait(subject,name)

            if 'forcejoin' in message.content:
                text=message.content.split()
                subject=text[1]
                name=text[2]
                try:
                    attend(subject,name)
                except:
                    await message.author.send('error while joining')
                    
            

client.run(token)