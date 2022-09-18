from logging import exception
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

'''
This is for the program to get a voice, importing
voice from an API developed by microsoft called sapi5.
pyttsx3 is basically used by the program to actually speak
to the user. We can select the voice of our choice by sapi5
'''

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    '''
    Function for the program to
    make it to speak anything.
    '''
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<16: 
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am your Personal Assistant, how may I help you?")

def takeCommand():
    '''
    This function takes input from the user's 
    microphone and returns a string output
    '''
    r = sr.Recognizer()
    #source = sr.Microphone
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 #seconds of non-speakig audio before a phrase is considered complete
        audio = r.listen(source)

    try:
        print("Recognising...")
        userCommand = r.recognize_google(audio, language='en-in')
        print(userCommand)
    except Exception as e:
        print("Would you say that again, please?")
        return "None"
    return userCommand

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Please wait...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("www.youtube.com")
    
        elif 'google' in query:
            speak("Opening Google")
            webbrowser.open("www.google.com")
  
        elif 'linkedin' in query:
            speak("Opening LinkedIn")
            webbrowser.open("www.linkedin.com")

        elif 'amazon' in query:
            speak("Opening Amazon")
            webbrowser.open("www.amazon.in")

        elif 'moodle' in query:
            speak("Opening Gitam Learning Management System")
            webbrowser.open("learn.gitam.edu")

        elif 'prime' in query:
            speak("Opening Amazon Prime Video")
            webbrowser.open("www.primevideo.com")

        elif 'time' in query:
            strTime1 = datetime.datetime.now().strftime("%H")
            strTime2 = datetime.datetime.now().strftime("%M")
            if int(strTime1)>12:
                ap="P M"
            else:
                ap="A M"
            speak(f"The time is {strTime1}{strTime2}{ap}")
    
        elif 'quit' in query:
            speak("Good Bye")
            break