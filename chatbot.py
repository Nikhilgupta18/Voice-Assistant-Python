import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pyttsx3


engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
# for i in range(len(voices)):
#     if voices[i].gender == 'male':
#         print(voices[i].id)
# print(voices[10].id)

engine.setProperty('voice', voices[10].id)
# engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am The Prototype1. How may I help you")


def takeCommand():  # it takes mic input and returns the string as output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please....")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching .....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        if 'search' in query:
            speak("Searching .....")
            query = query.replace("search", "")
            webbrowser.open("https://google.com/search?q=%s" % query)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com")

        elif 'open gmail' in query:
            webbrowser.open("https://www.gmail.com")

        elif 'open google' in query:
            webbrowser.open("https://google.com")


# 10 11 29 51
