import ctypes
import datetime
import shutil
import ecapture as ec
import winshell as winshell
import wolframalpha
import pyjokes as pyjokes
import wikipedia
import webbrowser
import speech_recognition as sr
import pyttsx3
import json
import os
import smtplib
import subprocess
from time import sleep
import requests
from bs4 import BeautifulSoup
import re
from datetime import date
import pyautogui
from urllib.request import urlopen
from playsound import playsound
import keyboard
from pynput.keyboard import Key,Controller
from time import sleep
import random
import pywhatkit
import GreetMe
import requests
from geopy.geocoders import Nominatim
from bs4 import BeautifulSoup
from newspaper import Article
# from digidevice import location
# from pyttsx3.drivers._espeak import Key

# from flask import Flask,request

# keyboard = Controller()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
 engine.say(audio)
 engine.runAndWait()


dictapp = {"commandprompt":"cmd","paint":"paint","word":"winword", "excel":"excel","chrome":"chrome","vscode":"code", "powerpoint":"powerpnt","notepad":"notepad.exe","calculator":"calc.exe"}

def list_doc():
    req = requests.get("https://www.practo.com/search/doctors?results_type=doctor&q=%5B%7B%22word%22%3A%22doctor%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22common_name%22%7D%5D&city=Mumbai")

    soup = BeautifulSoup(req.content, "html.parser")

    articles = soup.find_all('div', class_='listing-doctor-card')
    for item in articles:
        h2 = ', '.join([x.get_text() for x in item.find_all('h2')])
        print(h2)
        speak(h2)


def locations():
    # initialize Nominatim API
    geolocator = Nominatim(user_agent="geoapiExercises")

    urlopen("http://ipinfo.io/json")

    data = json.load(urlopen("http://ipinfo.io/json"))

    lat = data['loc'].split(',')[0]

    lon = data['loc'].split(',')[1]

    # Latitude & Longitude input
    Latitude = lat
    Longitude = lon

    location = geolocator.reverse(Latitude + "," + Longitude)

    address = location.raw['address']

    # traverse the data
    city = address.get('city', '')
    state = address.get('state', '')
    country = address.get('country', '')
    code = address.get('country_code')
    zipcode = address.get('postcode')
    print('City : ', city)
    print('State : ', state)
    print('Country : ', country)
    print('Zip Code : ', zipcode)



def takeCommand():
    #It takes microphone input and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
       print("Listening.....")
       r.pause_threshold = 0.5
       r.energy_threshold = 300
       r.dynamic_energy_threshold = True
       audio = r.listen(source, 0, 4)

       try:
         print("Recognizing....")
         query = r.recognize_google(audio,language = 'en-in')
         print(f"User said  {query}\n")
       except Exception as e:
        #print(e)
        print("Say that again please")
        return "None"
    return query



if __name__ == '__main__':

   while True:
       #if 1:
       locations()
       query = takeCommand().lower()
       if "need help" in query:
           from GreetMe import greetMe

           greetMe()


           while True:

            query = takeCommand().lower()

            # Logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)


            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'how are you' in query:
                speak(" I Am Fine,Thank you")
                speak("How are You,Sir")

            elif 'fine' in query or'good' in query:
                speak("I am Happy to know that ")

            elif 'who made you' in query:
                speak(" I have been created by Bigo4")

            elif 'who are your friends' in query:
                speak("My Friends are Alexa and Siri")

            elif 'exit' in query or 'stop' in query:
                speak("Thanks for giving me your time,Sir")
                exit()
            elif 'what is your name' in query:
                speak("my Name is Bigo4 Assitent")

            elif 'joke' in query:
                speak(pyjokes.get_joke())

            elif "change my name to" in query:
                speak("What would you like to call me,Sir")
                query = query.replace("change my name to","")
                assname = query
                speak("That is a good one,Sir!")

            elif 'change name' in query:
                speak("What would you like to call me,Sir")
                assname = takeCommand()
                speak("My Friends Call me that")

            elif 'thank you' in query:
                speak("Always Available Sir,anytime")

            elif 'welcome' in query:
                speak("I think i should say that")

            elif 'who am i' in query:
                speak("If you can talk then definetly you are human")

            elif 'why you came to the world' in query:
                speak("Thanks to Bigo$. further It's a Secret")

            elif 'camera' in query or'take a photo' in query:
                ec.capture(0,"Jarvis Camera","img.jpg")


            elif "temperature" in query:
                search = "temperature in varanasi"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak(f"current{search} is {temp}")
            elif "weather" in query:
                search = "temperature in varanasi"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak(f"current{search} is {temp}")

    # Set An Alarm
            elif "alarm" in query:
                speak("Enter the Time!")
                time = input(":Enter the time")

                while True:
                    Time_Ac = datetime.datetime.now()
                    now = Time_Ac.strftime("%H:%M:%S")

                    if now == time:
                        speak("Alarm Is Ringing")
                        playsound("music.mp3")
                        speak("Alarm Closed")

                    elif now>time:
                        break
            # --------------------------------Health Functions-----------------------

            elif "doctor near me":
                list_doc()

            elif " book an appoinment" in query:
                speak("booking")

            elif "sleep" in query:
                speak("Going to sleep,sir")
                exit()


