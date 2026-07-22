
# voice assistent

import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import pyjokes 
import os
import time
import random as r
def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = recognizer.listen(source)  # <- yaha source diya jaruri hai
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Sorry, I did not get that")

def speechtx(x):
    engine =  pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()




if __name__  == '__main__':

    if sptext().lower() == "alexa": 
        speechtx("hi hitesh")
        while True:
            data1 = sptext().lower()
            if "your name" in data1:
                name = "my name is Alexa"
                speechtx(name)
            elif "old are you" in data1:
                age = "i am two years old"
                speechtx(age)

            elif 'time' in data1:
                time = datetime.datetime.now().strftime("%I:%M%p")
                print(time)
                speechtx(time)

            elif 'open youtube' in data1:
                webbrowser.open("https://www.youtube.com/")

            elif "joke" in data1:
                joke_1 = pyjokes.get_joke(language="en",category='neutral')
                print(joke_1)
                speechtx(joke_1)

            elif 'play song' in data1:
                add = "C:\Python Course\Python_Project\Jarvis voice Assistent\song"
                listsong =  os.listdir(add)
                songs = r.choice(listsong)
                print(listsong)
                os.startfile(os.path.join(add,songs))
            
            elif "exit" in data1:
                speechtx("thank you")
                break

            time.sleep(5)




    else:
         print("thanks")

        



