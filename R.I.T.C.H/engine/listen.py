import speech_recognition as sr

def get_audio():

    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(" I am Listening...")
        r.phrase_time_limit=10
        audio = r.listen(source)

    try:   
        said = r.recognize_google(audio, language='en-in')
        print(f"Aaryan said: {said}\n")
    except: 
        return "None"
    return said



while True:
    get_audio()