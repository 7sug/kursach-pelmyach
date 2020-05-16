import speech_recognition as sr
import pyttsx3

def speak(what):
    print( what )
    speak_engine.say( what )
    speak_engine.runAndWait()
    speak_engine.stop()

def helper():
    speak('я умею показывать места на карте, умею искать в гугле, умею говорить время, умею говорить погоду, умею производить простые вычисления')
    speak('уточните команду для подробностей')
def time():
    speak('чтобы узнать время, скажи галя который час или галя сколько времени')

def google():
    speak('поиск в гугле осуществляется командой галя найди')

def calc():
    speak('я умею делить, умножать, складывать и вычитать. Отвечу на любой вариант фразы, можешь не переживать')

def loc():
    speak('найти что-то на карте можно командой галя где или галя покажи')

def weath():
    speak('чтобы узнать погоду скажи галя погода ваш город')

speak_engine = pyttsx3.init()
voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[4].id)
