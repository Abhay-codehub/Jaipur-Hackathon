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
from twilio.rest import Client
import keys
import pandas as pd
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
import requests
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


# def avl_beds() :



def show_hospital():
    req = requests.get(
        "https://www.practo.com/search/hospitals?results_type=hospital&q=%5B%7B%22word%22%3A%22hospital%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22type%22%7D%5D&city=Jaipur")
    link1 = "https://www.practo.com/search/hospitals?results_type=hospital&q=%5B%7B%22word%22%3A%22hospital%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22type%22%7D%5D&city=Jaipur"
    soup = BeautifulSoup(req.content, "html.parser")

    # -----------------------------

    # for h2 in h2:
    articles = soup.find_all('div', class_='c-estb-info')
    for item in articles:
        a2 = ', '.join([x.get_text() for x in item.find_all('a')])
        print(a2)
        speak(a2)
        send_msg(link1)


def list_doc():

    req = requests.get(
        "https://www.practo.com/search/doctors?results_type=doctor&q=%5B%7B%22word%22%3A%22doctor%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22common_name%22%7D%5D&city=Mumbai")
    link = "https://www.practo.com/search/doctors?results_type=doctor&q=%5B%7B%22word%22%3A%22doctor%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22common_name%22%7D%5D&city=Mumbai"
    soup = BeautifulSoup(req.content, "html.parser")

    # -----------------------------

    # for h2 in h2:
    articles = soup.find_all('div', class_='listing-doctor-card')
    for item in articles:
        h2 = ', '.join([x.get_text() for x in item.find_all('h2')])
        print(h2)
        speak(h2)


    print("For Appointment and more Information a link is being send shortly." )
    send_msg(link)

def show_hospital():
    req = requests.get(
        "https://www.practo.com/search/hospitals?results_type=hospital&q=%5B%7B%22word%22%3A%22hospital%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22type%22%7D%5D&city=Jaipur")
    link1 = "https://www.practo.com/search/hospitals?results_type=hospital&q=%5B%7B%22word%22%3A%22hospital%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22type%22%7D%5D&city=Jaipur"
    soup = BeautifulSoup(req.content, "html.parser")

    # -----------------------------

    # for h2 in h2:
    articles = soup.find_all('div', class_='c-estb-info')
    for item in articles:
        a2 = ', '.join([x.get_text() for x in item.find_all('a')])
        print(a2)
        speak(a2)

    print("For Appointment and more Information a link is being send shortly.")
    send_msg(link1)

def read_data():
    data = pd.read_csv(r'C:\Users\nites\OneDrive\Documents\GitHub\Jaipur-Hackathon\ABHACARD DATA DEMO.csv')
    df = pd.DataFrame(data, columns=['bmi'])
    speak(df)

def send_msg(str):
    client = Client(keys.account_sid, keys.auth_token)

    # message = client.messages.create(
    #     body= " Shared Link :-" + str,
    #     from_=keys.twilio_number,
    #     to=keys.my_phone_number
    # )
    print("message sent")


def make_call():
    client = Client(keys.account_sid, keys.auth_token)

    call = client.calls.create(
        url="http://demo.twilio.com/docs/voice.xml",
        to=keys.my_phone_number,
        from_=keys.twilio_number
    )
    print("Call Done")

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
       #1:
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

            elif 'Availiblity of beds' in query:
                speak("If you can talk then definetly you are human")

            elif 'doctor' in query:
                list_doc()
                break

            elif "hospital":
                show_hospital()
                break


            elif " book an appoinment" in query:
                speak("booking")

            elif "sleep" in query:
                speak("Going to sleep,sir")
                exit()


