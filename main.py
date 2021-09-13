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
import wikipedia


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


# return the weekday name
def query_day():
    day = datetime.date.today()
    print(day)
    weekday = day.weekday()
    print(weekday)
    mapping = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    try:
        speaking(f'Today is {mapping[weekday]}')
    except:
        pass


# return the time
def query_time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speaking(f"{time[0:2]} o'clock and {time[3:5]} minutes")


# Intro greeting at startup
def whatsup():
    speaking('''Hi, my name is Avivi. I am your personal assistant.
     how may i help you?''')


# the heart of our assistant. Take queries and returns answers.
def querying():
    whatsup()
    start = True
    while start:
        q = transform().lower()
        if 'start youtube' in q:
            speaking('Starting youtube. Just a second')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'start web browser' in q:
            speaking('open browser')
            webbrowser.open('https://www.google.com')
            continue
        elif 'what day is it' in q:
            query_day()
            continue
        elif 'what time is it' in q:
            query_time()
            continue
        elif 'shutdown' in q:
            speaking('ok. I am shutting down')
            break
        elif 'from wikipedia' in q:
            speaking('Checking wikipedia')
            # this removes the word wikipedia from the search
            q = q.replace("wikipedia", "")
            results = wikipedia.summary(q, sentences=2)
            speaking('found on wikipedia')
            speaking(results)
            continue
        elif 'your name' in q:
            speaking('I am Avivi. Your VA')
            continue
        elif 'search web' in q:
            pywhatkit.search(q)
            speaking('that is what i found')
            continue
        elif 'play' in q:
            speaking(f'Playing {q}')
            pywhatkit.playonyt(q)
            continue
        elif 'joke' in q:
            speaking(pyjokes.get_joke())
            continue
        elif 'stock price' in q:
            search = q.split("of")[-1]
            lookup = {'apple': 'AAPL', 'amazon': 'AMZN', 'google': 'GOOGL'}
            try:
                stock = lookup[search]
                stock = yf.Ticker(stock)
                current_price = stock.info["regularMarketPrice"]
                speaking(f'found it, the price for {search} is {current_price}')
            except:
                speaking(f'sorry i have no data for {search}')
            continue


if __name__ == '__main__':
    transform()
