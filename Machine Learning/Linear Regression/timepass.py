import pyttsx3
import datetime
import speech_recognition as sr
engine = pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print("DragonZpyder: " +audio)


def get_audio():

    #It tane input from the user and returns string outputkes micropho

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(" I am Listening...")
        r.pause_threshold=1
        audio = r.listen(source)

        try:
            said = r.recognize_google(audio,language='en-in')
            print(f"said: {said}\n")
        
        except:
            pass
        
        return said

# speak(f"Good morning sir . Its {str(datetime.datetime.now())[11:16]} in the morning . It's raining outside sir . If you happen to go out today, dont forget to take your umbrella with you") 

# speak("Mum is very angry on you . ")
# speak("Everyone woke up at 6 today . ")

# speak("Yesterday there has been a positive change on the stock market . ")
# speak("The Nepal Stock Exchange increased by 161 points . ")
# speak("Now I think you can start investing on the stock market . Maybe I can confirm the start of the bullish trend in the stock market . ")

a = get_audio()



