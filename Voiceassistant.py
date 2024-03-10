import speech_recognition as sr
import pyttsx3

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Could you please repeat?")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if '_name_'=="main_":
    speak("Hello! I'm your voice assistant. How can I help you today?")

while True:
        user_input = listen()

        if "quit" in user_input:
            speak("Goodbye!")
            break
        elif "hello" in user_input:
            speak("Hi there! How can I assist you?")
        else:
            speak("I'm not sure how to respond to that. Please ask me something else.")

