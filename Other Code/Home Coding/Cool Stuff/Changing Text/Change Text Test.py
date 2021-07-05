from gtts import gTTS
import subprocess
import time
import os
def MakePlayText():
        textyu=input()
        mytext =  textyu
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save(textyu+".mp3")   

while 1==1:
    MakePlayText()
