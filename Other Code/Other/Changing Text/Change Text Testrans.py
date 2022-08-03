from gtts import gTTS
import subprocess
import time
import os
import random
from random_word import RandomWords
from vocabulary.vocabulary import Vocabulary as vb
r = RandomWords()
randword = r.get_random_word()
file = randword+'.mp3'
word = randword
#times
def PlayText():
        mytext =  word+'tastes like'+word
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save(file)
        time.sleep(1)
        subprocess.call(file, shell=True)
PlayText()
