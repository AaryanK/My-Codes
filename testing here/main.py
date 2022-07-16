import datetime
from pydub import AudioSegment
from pydub.playback import play



from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math
# Get default audio device using PyCAW
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# Get current volume 
currentVolumeDb = volume.GetMasterVolumeLevel()



alarmtime = '04:30'
time = datetime.datetime.now().strftime('%H')+':'+datetime.datetime.now().strftime('%M')
while True:
    time = datetime.datetime.now().strftime('%H')+':'+datetime.datetime.now().strftime('%M')
    if time == alarmtime:
        volume.SetMasterVolumeLevel(0.0, None)
        for i in range(2):
        	music = AudioSegment.from_mp3('alarm.mp3')
        	play(music)
