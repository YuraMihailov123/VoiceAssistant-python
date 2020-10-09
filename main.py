import speech_recognition as sr
import os
from googlesearch import search
import pyaudio
import sys
import webbrowser

def talk_to_user(words):
    print(words)
    os.system("say " + words)

def listen_from_user():
     r = sr.Recognizer()

     with sr.Microphone() as source:
         print("Говорите")
         r.pause_threshold = 1
         r.adjust_for_ambient_noise(source,duration=1)
         audio = r.listen(source)

     try:
         task = r.recognize_google(audio, language="ru-RU").lower()
         print("Вы сказали: " + task)
     except sr.UnknownValueError:
         talk_to_user("Не распознана команда!")
         task = listen_from_user()

     return task

def do_actions(action):
    if 'найди' in action:
        query = action.split(" ",1)[1].strip()
        search_google_possible_links(query)



def search_google_possible_links(query):

    for j in search(query, tld="com", lang="ru", num=10, stop=10, pause=2):
        print(j)

talk_to_user("Привет")
while True:
    do_actions(listen_from_user())