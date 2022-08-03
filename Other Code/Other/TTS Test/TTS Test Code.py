from gtts import gTTS
import urllib3
urllib3.disable_warnings()
import certifi
import subprocess
import time
import os
http = urllib3.PoolManager(
      cert_reqs='CERT_REQUIRED',
      ca_certs=certifi.where())
def MakePlayText():
    if os.path.isfile('fune.mp3'):
        subprocess.call('fune.mp3', shell=True)
    else:
        mytext = 'Hahaha, so funny'
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("fune.mp3")   

MakePlayText()

