import webbrowser
def loc(voice):
    voice = voice.split(" ")
    if 'где' in voice:
        voice.remove('где')
    elif 'покажи' in voice:
        voice.remove('покажи')
    location = ' '.join(voice)
    webbrowser.open("https://www.google.nl/maps/place/" + location + "/&amp;")
