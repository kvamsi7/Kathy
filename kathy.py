
# Necessay imports
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests

# setting the kathy's (Virtual Assistant voice)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
for voice in voices:
    print("ID: %s" % voice.id)
    print("Name: %s" % voice.name)
    print("Age: %s" % voice.age)
    print("Gender: %s" % voice.gender)
    print("Languages Known: %s" % voice.languages)
engine.setProperty('voice', 'voices[0].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()


def wish_me():
    hour = datetime.datetime.now().hour
    if hour > 0 and hour < 12:
        speak("Hello, Good Morning")
        print("Hello, Good Morning")
    elif hour > 12 and hour < 18:
        speak('Hello, Good Afternoon')
        print('Hello, Good Afternoon')
    else:
        speak('Hello, Good Evening')
        print('Hello, Good Evening')

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio,language='en-in')
            print(f"user said : {statement}")
        
        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement
print("Loading the Virtual Assistant Kathy")
speak("Loading the Virtual Assistant Kathy")
wish_me()

if __name__ == '__main__':

    while True:
        speak("Tell me how can i help you now ?")
        statement = take_command().lower()
        if statement == 0:
            continue
        
        if 'good bye' in statement or "ok bye" in statement or "stop" in statement:
            speak("sure, Thanks for having me, Hope you have good one, Good bye")
            print("sure, Thanks for having me, Hope you have good one, Good bye")
            break
        
        elif 'wikipedia' in statement:
            speak('Searching Wikipedia')
            statement = statement.replace("wikipedia","")
            results = wikipedia.summary(statement,sentences = 3)
            try:
                speak("According to Wikipedia")
            except PageError as p:
                print(f"Exception {p}")
            print(results)
            speak(results)
        
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)
        
        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrom is open now")
            time.sleep(5)
        
        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://www.gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif 'time' in statement:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {str_time}")

        elif "news" in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak("Here are some headlines from the Times of India, Happy reading")
            time.sleep(6)

        elif 'camera' in statement or "take a photo" in statement:
            try:
                ec.capture(0,"robo camera","img.jpg")
            except Exception as e:
                print(f"Exception {e} occured")

        elif "search" in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
        
        elif "ask" in statement:
            speak("I can answer to computational and geographical questions \
                and what question do you want to ask now")
            question = take_command()
            app_id = "Paste your unique ID here"
            tr
            client = wolframalpha.Client("#appid")
            res = client.query(question)
            answer = next(nes.results).text
            speak(answer)
            print(answer)

        elif 'who are you' in statement or 'what can you do' in statement:
            speak("I am Kathy version point 1 personal assistant.\
                I am programmed to minor tasks like opening youtube, google chrome, gmail and stackoverflow,\
                 predict time, take a photo, search wikipedia, predict weather")
            
        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Vamsi")
            print("I was built by Vamsi")
        
        elif "how are you" in statement:
            speak("I'm fine, Thank you. Hope you are fine aswell")
            print("I'm fine, Thank you. Hope you are fine aswell")
        
        elif "log off" in statement or "sign out" in statement:
            speak("Are you sure")
            speak("Are you sure")
            statement = take_command()
            if "yes" in statement or "yup" in statement:
                speak("ok, your pc will log off in 10 sec make sure you exit from all applications")
                subprocess.call(["shutdown","/1"])
        
        