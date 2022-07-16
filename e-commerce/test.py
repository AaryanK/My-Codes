import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print("DragonZpyder: " +audio)


def get_audio():

    #It takes input from the user and returns string outputkes micropho

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('I am listening')
        r.phrase_time_limit=10
        audio = r.listen(source)

    try:   
        said = r.recognize_google(audio, language='en-us')
        print(f'Aaryan said: {said}\n')
    except: 
        return "None"
    return said



text = get_audio()


print(text)