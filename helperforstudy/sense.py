import os


def speak(audio):
    os.system(f'echo \"{audio}\" | festival --tts')