import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia

# Initialize voice engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except:
        speak("Sorry, I could not understand.")
        return ""

def assistant():
    speak("Hello Muzammil, I am your Voice Assistant.")

    while True:
        command = listen()

        if "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {current_time}")

        elif "google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "wikipedia" in command:
            speak("What do you want to search?")
            query = listen()

            try:
                result = wikipedia.summary(query, sentences=2)
                speak(result)
            except:
                speak("No information found.")

        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break

        elif command != "":
            speak("Command not recognized.")

assistant()