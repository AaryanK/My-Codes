# import pyttsx3
# import speech_recognition as sr
import json

# engine = pyttsx3.init()
# engine.setProperty('rate',150)
# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# def get_audio():
#
#     #It tane input from the user and returns string outputkes micropho
#
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print(" I am Listening...")
#         r.adjust_for_ambient_noise(source,0.2)
#         # r.phrase_time_limit=10
#         audio = r.listen(source)
#
#     try:
#         said = r.recognize_google(audio, language='en-uk')
#     except:
#         return "None"
#     return said.lower()


intents = json.loads(open('intents.json').read())

from train import predict,get_response

print('Come on lets talk Aaryan')
while True:
    message = input("Enter a mesesage here : ")
    ints = predict(message)
    res = get_response(ints,intents)
    print(res)
    if res in ["Bye","See you soon","Okay,bye have a nice one"]:
        break