import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import pyjokes
from datetime import date


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',125)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            listener.pause_threshold = 0.5
            voice = listener.listen(source)
            command = listener.recognize_google(voice,language='en-in')
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
    except:
        pass
    return command

    

def run_jarvis():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '', 1)
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('It is ' + time)
    elif 'date' in command:
        d = date.today().strftime("%B %d")
        talk("Today's date is " + d)
    elif 'search for' in command:
        person = command.replace('search', '')
        info = wikipedia.summary(person, 1)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


run_jarvis()
