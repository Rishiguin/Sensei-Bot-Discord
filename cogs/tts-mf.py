import os
from gtts import gTTS
import pyttsx3

text_to_read = "teri gaand maar dunga madarchod"

filename = 'my_file.mp3'


def female(text,dia):
    language = f'en-{dia}'
    slow_audio_speed = False
    audio_created = gTTS(text=text, lang=language,
                         slow=slow_audio_speed)
    audio_created.save(filename)

def male(text):
    engine=pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.save_to_file(text_to_read, filename)
    engine.runAndWait()