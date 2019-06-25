from pygame import mixer
from gtts import gTTS
import winsound
from pathlib import Path

class SOUND:
    async def openDoor(self):

        f = "sounds/door_opened.mp3"
        mixer.init(frequency=23100)
        mixer.music.load(f)
        mixer.music.play()

    async def welcome(text):
        f = "sounds/"+text+".mp3"
        if(not Path(f).exists()):
            tts = gTTS(text="Hoşgeldin "+text, lang='tr')
            tts.save(f)

        mixer.init(frequency=23100)
        mixer.music.load(f)
        mixer.music.play()


    async def beep(self):
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 300  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
