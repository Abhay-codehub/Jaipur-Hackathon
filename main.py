
import speech_recognition as sr
import pyttsx3
import json
from twilio.rest import Client
import keys
from urllib.request import urlopen
from geopy.geocoders import Nominatim
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
 engine.say(audio)
 engine.runAndWait()


dictapp = {"commandprompt":"cmd","paint":"paint","word":"winword", "excel":"excel","chrome":"chrome","vscode":"code", "powerpoint":"powerpnt","notepad":"notepad.exe","calculator":"calc.exe"}


def take_med(str1):
    int = 1

    while int == 1:
        named_tuple = time.localtime()  # get struct_time
        time_string = time.strftime("%H:%M:%S", named_tuple)
        client = Client(keys.account_sid, keys.auth_token)

        # time_string1 = time.strftime()

        if (time_string == str1):
            message = client.messages.create(
                body="You will win the hackathon",
                from_=keys.twilio_number,
                to=keys.my_phone_number
            )

    time.sleep(1)


def pain_killer():
    with open('Meds price compo.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        row_count = 1
        for i in csv_reader:
            if row_count == 3:
                speak(i[3])
                speak("The price is RS 10 per strip")
            row_count += 1

def pracetamol():
    with open('Meds price compo.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        row_count = 1
        for i in csv_reader:
            if row_count == 2:
                speak(i[3])
                speak("The price is RS 15 per strip")
            row_count += 1

def blood_bank01() :
    text = '''1. B.D.Memorial Blood Centre || Plot No. 4&98 Neelkanth colony, Ajmer road near BPCL PETROL PUMP PURANICHUNGI, Jaipur, Jaipur, Rajasthan || Plot No. 4&98 Neelkanth colony, Ajmer road near BPCL PETROL PUMP PURANICHUNGI, Jaipur, Jaipur, Rajasthan || Phone: 9887318888 ,Fax: -, Email: bdmemorialbloodbank@gmail.com || Available, O+Ve:71, B+Ve:28, A+Ve:36, O-Ve:1, AB+Ve:4, B-Ve:1 || Last Updated 06-03-2023 13:47 ||

            2. Blood Centre Mahatma Gandhi Hospital || Blood Bank, M G Medical College and Hospital ,Mahatma Gandhi University of Medical Science and Technology, Sitapura,Jaipur, Jaipur, Jaipur, Rajasthan || Phone: 9116019981 ,Fax: -, Email: mghbloodbank@gmail.com || Available, O+Ve:1, B+Ve:1 || Last Updated : 20-03-2023 10:01 ||

            2. Govt Bdm Sat Hosp Kotputli || Govt BDM hospital Kotputli N.N 48, Kotputli, Jaipur, Rajasthan || Phone: 9116534500 ,Fax: -, Email: bloodbankkotputli@gmail.com || Available, O-Ve:1, O+Ve:35, A+Ve:19, B+Ve:43, AB-Ve:1, AB+Ve:6, A-Ve:4, B-Ve:3 || Last Updated : 19-03-2023 11:51  
    '''

    speak("Sending you required information shortly")
    send_msg(text)



def show_hospital():
    req = requests.get(
        "https://www.practo.com/search/hospitals?results_type=hospital&q=%5B%7B%22word%22%3A%22hospital%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22type%22%7D%5D&city=Jaipur")
    link1 = "https://www.practo.com/search/hospitals?results_type=hospital&q=%5B%7B%22word%22%3A%22hospital%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22type%22%7D%5D&city=Jaipur"
    soup = BeautifulSoup(req.content, "html.parser")

    # -----------------------------
    speak("The few hospitals near you are ")
    # for h2 in h2:
    articles = soup.find_all('div', class_='c-estb-info')
    for item in articles:
        a2 = ', '.join([x.get_text() for x in item.find_all('a')])
        print(a2)
        speak(a2)
        send_msg(link1)
        speak("Sending more information to you shortly")

def avl_oxg01() :
    with open('bedsRAJASTHAN.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        row_count = 1
        for i in csv_reader:
            if row_count == 2:
                print(i[4])
                speak(i[4])
            row_count += 1
        link_oxy_bed01 = "https://covidinfo.rajasthan.gov.in/COVID19HOSPITALBEDSSTATUSSTATE.aspx"
        speak("Sending You more information shortly.")
        send_msg(link_oxy_bed01)

def show_vent01():
    with open('bedsRAJASTHAN.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        row_count = 1
        for i in csv_reader:
            if row_count == 2:
                print(i[10])
                speak(i[10])
            row_count += 1
        speak("Sending you more information for that shortly.")
        link_oxy_bed01 = "https://covidinfo.rajasthan.gov.in/COVID19HOSPITALBEDSSTATUSSTATE.aspx"
        send_msg(link_oxy_bed01)

def avl_oxg02() :
    with open('bedsRAJASTHAN.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        row_count = 1
        for i in csv_reader:
            if row_count == 18:
                print(i[4])
                speak(i[4])
            row_count += 1
        link_oxy_bed02 = "https://covidinfo.rajasthan.gov.in/COVID19HOSPITALBEDSSTATUSSTATE.aspx"
        speak("Sending you more information for that shortly.")
        send_msg(link_oxy_bed02)

def show_vant02() :
    with open('bedsRAJASTHAN.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        row_count = 1
        for i in csv_reader:
            if row_count == 18:
                print(i[10])
                speak(i[10])
            row_count += 1
        link_oxy_bed02 = "https://covidinfo.rajasthan.gov.in/COVID19HOSPITALBEDSSTATUSSTATE.aspx"
        speak("Sending you more information for that shortly.")
        send_msg(link_oxy_bed02)

def list_doc():

    req = requests.get(
        "https://www.practo.com/search/doctors?results_type=doctor&q=%5B%7B%22word%22%3A%22doctor%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22common_name%22%7D%5D&city=Mumbai")
    link = "https://www.practo.com/search/doctors?results_type=doctor&q=%5B%7B%22word%22%3A%22doctor%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22common_name%22%7D%5D&city=Mumbai"
    soup = BeautifulSoup(req.content, "html.parser")

    # -----------------------------
    speak("The few doctors near you are")
    # for h2 in h2:
    articles = soup.find_all('div', class_='listing-doctor-card')
    for item in articles:
        h2 = ', '.join([x.get_text() for x in item.find_all('h2')])
        print(h2)
        speak(h2)


    speak("For Appointment and more Information a link is being send shortly." )
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

    speak("For Appointment and more Information a link is being send shortly.")
    send_msg(link1)


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
    speak("Shortly nearest ambulance will call you.")

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

            if 'alternate medicine for paracetamol' in query:
                pracetamol()

            if 'blood banks in jaipur' in query:
                blood_bank01()


            elif 'ventilator' in query:
                show_vent01()

            elif 'hospitals' in query:
                show_hospital()

            elif 'doctors' in query:
                list_doc();

            elif "oxygen beds in ajmer" in query:
                avl_oxg01()

            elif "oxygen beds in jaipur" in query:
                avl_oxg02()


            elif "need ambulance" in query:
                make_call()

            elif "scheduled medicine" in query: # Just for showing the testing part
                take_med("06:23:00")

            elif "sleep" in query:
                speak("Going to sleep,sir")
                exit()


