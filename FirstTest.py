import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha
import openai
import os

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
activate_word = "computer"

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))


def speak(text, rate = 120):
    engine.setProperty("rate", rate)
    engine.say(text)
    engine.runAndWait()

def parseCommand():
    listener = sr.Recognizer()
    print("listening for a command")

    with sr.Microphone() as source:
        listener.pause_threshold = 2
        input_speech = listener.listen(source)

    try:
        print("recognizing speech")
        query = listener.recognize_google(input_speech, language="en_us")
        print("the input speech was: {query}")
    except Exception as exception:
        print("Couldn't catch that")
        speak("Couldn't catch that")
        print(exception)
        return 'None'

    return query

if __name__ == '__main__':
    speak("All systems nominal.")

    while True:
        query = parseCommand().lower().split()

        if query[0] == activate_word:
            query.pop(0)

            if query[0] == 'say':
                if 'hello' in query:
                    speak("Greetings")
                else:
                    query.pop(0)
                    speech = ' '.join(query)
                    speak(speech)
            if query[0] == "go" and query[1] == 'to':
                print("Opening...")
                query = " ".join(query[2:])
                webbrowser.get("chrome").open_new(query)
