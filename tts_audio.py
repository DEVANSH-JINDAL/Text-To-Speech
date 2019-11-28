import pyttsx3
from gtts import gTTS
engine = pyttsx3.init()
engine.setProperty('rate',150)
engine.say("hello")
f=open("new.txt","r")
for x in f.readlines():
    engine.say(x)
    engine.runAndWait()
f.close()
o=open("new.txt","r")
tts = gTTS(text=o.read(), lang='en')
tts.save("save.mp3")
print("File saved!")
engine.stop
o.close()