import speech_recognition as sr
import pyttsx3
def calc(voice):
    voice = voice.split(" ")
    #if 'посчитай' in voice:
    #    voice.remove('посчитай')
    if "+" in voice:
        c = (int(voice[0]) + int(voice[2]))
        speak(str(voice[0]) + " плюс " + str(voice[2]) + " будет " + str(c))
    elif ("x" in voice) or ("х" in voice):
        if "на" in voice:
            c = (float(voice[0]) * float(voice[3]))
            speak(str(voice[0]) + " умножить на " + str(voice[3]) + " будет " + str(c))
        else:
            c = (float(voice[0]) * float(voice[2]))
            speak(str(voice[0]) + " умножить на " + str(voice[2]) + " будет " + str(c))
    elif "/" in voice:
        c = (float(voice[0]) / float(voice[2]))
        speak(str(voice[0]) + " разделить на " + str(voice[2]) + " будет " + str(c))

    elif "-" in voice:
        c = (int(voice[0]) - int(voice[2]))
        speak(str(voice[0]) + " минус " + str(voice[2]) + " будет " + str(c))


def speak(what):
    print( what )
    speak_engine.say( what )
    speak_engine.runAndWait()
    speak_engine.stop()


speak_engine = pyttsx3.init()



voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[4].id)
