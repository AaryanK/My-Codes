import pyttsx3




class Speak:
    def __init__(self) -> None:
        self.engine = pyttsx3.init()
    def speak(self,audio,gender="MALE"):
        engine = self.engine
        voices = ['MALE','FEMALE']
        voice_index = voices.index(gender)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[voice_index].id)
        engine.save_to_file(audio, 'test.mp3')
        engine.runAndWait()
        engine.runAndWait()
        print("T.I.T.S: " +audio)

Speak().speak("Good Morning Sir;Its 6 in the morning ; you have school today;You had set an alarm for it",gender="FEMALE")


