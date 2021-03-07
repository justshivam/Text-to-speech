import pyttsx3

print('Welcome to Text-to-Speech engine.')
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

while(True):
    text = input('Enter text to be spoken: ')
    if text == 'quit':
        break
    engine.say(text)
    engine.runAndWait()