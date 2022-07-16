import datetime
import playsound




def play(music):
	playsound.playsound(music)


alarmtime = '04:30'
time = datetime.datetime.now().strftime('%H')+':'+datetime.datetime.now().strftime('%M')
while True:
    time = datetime.datetime.now().strftime('%H')+':'+datetime.datetime.now().strftime('%M')
    if time == alarmtime:
        for i in range(2):
        	play('matchday.mp3')
