import pyttsx3


def speak(audio,voice=0):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice].id)
    engine.say(audio)
    engine.runAndWait()



    


# speak("Hello Aaryan",1)