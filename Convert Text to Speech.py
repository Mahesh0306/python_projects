from gtts import gTTS
import os
mytext = 'hello world'
language = "en"
myobject = gTTS(text=mytext, lang=language, slow=False)
myobject.save("welcome.mp3")
os.system("welcome.mp3")