import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
from modules import main
voice = ''
main.speak('Привет. Что-то надо?')
while True:
    voice = main.recordAudio()
