import pyttsx3 
engine = pyttsx3.init()

def speak(input_data):
    engine.say(input_data)
    engine.runAndWait()
    engine.stop()

def text_to_speech():
    text = input('Введите текст: ')
    if text:
        speak(text)

while True:
    text_to_speech()