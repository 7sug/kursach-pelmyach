import webbrowser
import urllib.parse
def search(voice):
    voice = voice.split(" ")
    if 'поищи' in voice:
        voice.remove('поищи')
    elif 'найди' in voice:
        voice.remove('найди')
    voice = ' '.join(voice)
    tes = urllib.parse.quote_plus(voice)
    webbrowser.open('https://www.google.com/search?q=' + tes +'&ie=utf-8&oe=utf-8&client=firefox-b-ab')
