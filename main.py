import speech_recognition as sr
import os
from googlesearch import search
import asyncio
from appscript import *
import pyaudio
import sys
import webbrowser

safari = app("Safari")
linkArr = []
indexLink = 0

def talk_to_user(words):
    print(words)
    os.system("say " + words)


def listen_from_user():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говорите")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio, language="ru-RU").lower()
        print("Вы сказали: " + task)
    except sr.UnknownValueError:
        talk_to_user("Не распознана команда!")
        task = listen_from_user()

    return task


def do_actions(action):
    if 'поиск' in action:
        asyncio.run(search_logic(action))
    if 'следующее' in action:
        global indexLink
        indexLink += 1
        open_url(linkArr[indexLink])




async def search_logic(action):
    query = action.split(" ", 1)[1].strip()
    await search_google_possible_links(query)
    talk_to_user("Найдено " + str(len(linkArr)) + " результатов по запросу " + query)
    open_url(linkArr[indexLink])
    await asyncio.sleep(5)
    do_actions("следующее")
    #close_current_tab_in_browser()


def open_url(url):
    #safari.make(new=k.document, with_properties={k.URL: url})
    print(url)
    safari.windows.first.current_tab.URL.set(url)

def close_current_tab_in_browser():
    safari.windows.first.current_tab.close()



async def search_google_possible_links(query):
    for j in search(query, tld="com", lang="ru", num=10, stop=10, pause=2):
        linkArr.append(j)


talk_to_user("Привет")
#while True:
    # do_actions(listen_from_user())
do_actions("поиск яблоко это")
