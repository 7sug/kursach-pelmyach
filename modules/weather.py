import pyowm
def weather(voice):
    voice = voice.split(" ")
    if 'погода' in voice:
        voice.remove('погода')
    voice = ' '.join(voice)
    owm = pyowm.OWM('983cd71369086bf29f5f16b8438bf9fd',language='ru')
    observation = owm.weather_at_place(voice)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')['temp']
    wind = w.get_wind()['speed']
    return temp
def wind(voice):
    voice = voice.split(" ")
    if 'погода' in voice:
        voice.remove('погода')
    voice = ' '.join(voice)
    owm = pyowm.OWM('983cd71369086bf29f5f16b8438bf9fd',language='ru')
    observation = owm.weather_at_place(voice)
    w = observation.get_weather()
    wind = w.get_wind()['speed']
    return wind
