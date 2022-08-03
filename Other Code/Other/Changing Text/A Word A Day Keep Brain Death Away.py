#The things i import
from gtts import gTTS
import subprocess
import time
import os
from random_word import RandomWords
from PyDictionary import PyDictionary
#Defining some variables and stuff
r = RandomWords()
#this gets the random word and checks if it has a dictionary definition, and makes the audio file
dictionary=PyDictionary()
randword = r.get_random_word(hasDictionaryDef="true")
#randword = 'wqw'
file = randword+' Definition.mp3'
#this part gets the meaning and converts the meaning into a string so it can say the text
toodefine = str(dictionary.meaning(randword))
if toodefine == 'None':
        toodefine = 'Sorry fam, there no definition, try again fam, sorry, sorry, sooooorry'
        todefine = toodefine
else:
        todefine = str(randword)+toodefine

texty = str(todefine)
#What makes the text, then plays it
def PlayText():
        #this part makes the file
        language = 'en'
        myobj = gTTS(text=texty, lang=language, slow=False) 
        myobj.save(file)
        #these prints are for debugging, randword is the random word, todefine is the definition
        print(randword)
        #texty is probably false, unless this has been fixed, and actaully define sthe word.
        print(texty)
        subprocess.call(file, shell=True)

#this just calls the function where everything is happening
PlayText()
