import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime
from modules import calc,google,joke,location,skills,weather
import sys


# настройки
opts = {
    "alias": ('галя','галка','галечка','чудовище'),
    "tbr": ('скажи','расскажи','сколько','произнеси','находится','сколько','какая','в','посчитай','будет'),
    "cmds": {
        "time": ('текущее время','сейчас времени','который час'),
        "rofl": ('расскажи анекдот','рассмеши меня','ты знаешь анекдоты'),
        "where": ('где находится','покажи'),
        "calc": ('прибавить','умножить','разделить','степень','вычесть','поделить','x','+','-','/','х','сколько будет'),
        "google": ('поищи', 'найди'),
        "exit": ('завершить','выйти','закрыть'),
        "weather": ('погода','какая погода'),
        "help": ('помощь','команды','что ты умеешь','возможности','умения','твои навыки'),
        "helpweather": ('как узнать погоду','погода команды','помощь погода'),
        "helpcalc": ('как мне посчитать','помощь калькулятор','как делать вычисления','как мне считать'),
        "helploc": ('где я','карта','места на карте','искать на карте'),
        "helpgoogle": ('как искать в гугле','как гуглить','поиск','помощь гугл')
    }
}

# функции
def speak(what):
    print( what )
    speak_engine.say( what )
    speak_engine.runAndWait()
    speak_engine.stop()

def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Говорите....")
        audio = r.listen(source)
    try:
        global voice
        voice = r.recognize_google(audio, language = "ru-RU").lower()
        print("[log] Распознано: " + voice)
        if voice.startswith(opts["alias"]):
            cmd = voice
            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()
            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()
            voice = cmd
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])

    except sr.UnknownValueError:
        print("[log] Голос не распознан!")
    except sr.RequestError as e:
        print("[log] Неизвестная ошибка, проверьте интернет!")

def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c,v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt

    return RC

def execute_cmd(cmd):
    if cmd == 'time':
        # сказать текущее время
        now = datetime.datetime.now()
        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))

    elif cmd == 'where':
        speak('Сейчас покажу' )
        location.loc(voice)

    elif cmd == 'rofl':
        # рассказать анекдот
        b = joke.rand()
        speak(b)

    elif cmd == 'calc':
        calc.calc(voice)

    elif cmd == 'google':
        speak('Вот что я нашла...')
        google.search(voice)

    elif cmd == 'exit':
        speak('выключаюсь')
        sys.exit()

    elif cmd == 'weather':
        tempa = weather.weather(voice)
        wind = weather.wind(voice)
        speak('На улице '+ str(tempa) + ' градусов')
        speak('Скорость ветра '+ str(wind) +  ' метров в секунду')

    elif cmd == 'help':
        skills.helper()

    elif cmd =='helploc':
        skills.loc()

    elif cmd == 'helpgoogle':
        skills.google()

    elif cmd =='helpweather':
        skills.weath()

    elif cmd =='helpcalc':
        skills.calc()

    else:
        print('Команда не распознана, повторите!')

voice = ''
speak_engine = pyttsx3.init()

voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[4].id)

#speak('опять работать')

#while True:
#    voice = recordAudio()
