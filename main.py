# this module makes python talks to us
import pyttsx3
import speech_recognition as sr
# this library helps us open any type of browser
import webbrowser
import datetime
# allows for example to search and open youtube
import pywhatkit
# helps to shut down or restart the computer
import os
# allows to ask for stock price for example
import yfinance as yf
import pyjokes
import pyaudio


# listen to our microphone and return the audio as text using google
def transform():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        # when someone speaks we wait less then a second
        rec.pause_threshold = 0.8
        # said will contain the words we said
        said = rec.listen(source)
        try:
            print("I am listening")
            # here we use google service to translate audio to text file
            q = rec.recognize_google(said, language="en")
            return q
        except sr.UnknownValueError:
            print("Sorry i did not understand")
            return "I am waiting"
        except sr.RequestError:
            print("Sorry the service is down")
            return "I am waiting"


def speaking(message):
    # initiate an object that will be able to speak
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

if __name__ == '__main__':
    transform()
