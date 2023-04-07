
import pyttsx3 
engine = pyttsx3.init()

file_txt = input('type name of the file if it is in other repository type path: ')

with open(f'{file_txt}','r') as file:
    to_speak = file.read()

engine.say(to_speak,'pt-br')
engine.runAndWait()
engine.stop()