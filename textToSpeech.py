import sys
import pyttsx3

tts = pyttsx3.init()
print('Enter the text to speak, or QUIT to quit.')
while True:
     text = input('> ')

     if text.upper() == 'QUIT':
           print('Thanks for playing!')
           sys.exit()
     tts.say(text)  # Add some text for the TTS engine to say.
     tts.runAndWait()  # Make the TTS engine say it.