import speech_recognition as sr
import os
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


talk_to_user("Привет")
while True:
    listen_from_user()