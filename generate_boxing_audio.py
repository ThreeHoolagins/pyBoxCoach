from gtts import gTTS # type: ignore
import os
from boxing_moves import attack, defense, actions

language = "en"
save_path = "./Audio Resources/Boxing Audio"

myobj = []

for x in attack:
    myobj.append(gTTS(text=x, lang=language, slow=False))
for x in defense:
    myobj.append(gTTS(text=x, lang=language, slow=False))
for x in actions:
    myobj.append(gTTS(text=x, lang=language, slow=False))

for iteration, x in enumerate(myobj):
    x.save(f"{save_path}/{defense[iteration]}.mp3")
