import os
from gtts import gTTS
# Options
text_to_read = "This is just a test using GTTS, a Python package library"
language = 'en'
slow_audio_speed = False
filename = 'my_file.mp3'
def reading_from_string():
    audio_created = gTTS(text=text_to_read, lang=language,
                         slow=slow_audio_speed)
    audio_created.save(filename)
    os.system(f'start {filename}')