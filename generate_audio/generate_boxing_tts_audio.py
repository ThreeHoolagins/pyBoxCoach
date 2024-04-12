from gtts import gTTS
import os
from constants import FileLocationConstants, BoxingMovesConstants
language = "en"

for move in BoxingMovesConstants.ATTACK_MOVES:
    attackTTS = gTTS(text=move.move, lang=language, slow=False)
    attackTTS.save(f"{FileLocationConstants.AUDIO_SRC_PATH}/{move.move}.mp3")

for move in BoxingMovesConstants.DEFENSE_MOVES:
    defenseTTS = gTTS(text=move.move, lang=language, slow=False)
    defenseTTS.save(f"{FileLocationConstants.AUDIO_SRC_PATH}/{move.move}.mp3")

for option in BoxingMovesConstants.ACTION_OPTIONS:
    optionTTS = gTTS(text=option, lang=language, slow=False)
    optionTTS.save(f"{FileLocationConstants.AUDIO_SRC_PATH}/{option}.mp3")