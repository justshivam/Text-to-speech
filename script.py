import pyttsx3

engine = pyttsx3.init()

#These two lines are optional.
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 150)     # default speed is 200

# These two lines are completely optional. These change the voice from male to female.
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say("Hello World")

# these lines generate the mp3 file for the text provided
# engine.save_to_file('Hello World', 'test.mp3') 

engine.runAndWait()
