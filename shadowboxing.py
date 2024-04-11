import random
import time
from tqdm import tqdm
from playsound import playsound
from boxing_moves import attack, defense, actions, silence
from pydub import AudioSegment
from pydub.playback import play
import os
from pydub.utils import which
AudioSegment.converter = which("ffmpeg")
# Meme Generator
from os import listdir
from os.path import isfile, join
base_dir = r"c:\Users\Caleb\Desktop\Projects\Boxing Program"
mypath = "./Audio Resources/Boxing Audio"
onlyfiles = [f"{mypath}/{f}" for f in listdir(mypath) if isfile(join(mypath, f))]

def concatenate_audio_pydub(audio_clip_paths, output_path, verbose=1):
    """
    Concatenates two or more audio files into one audio file using PyDub library
    and save it to `output_path`. A lot of extensions are supported, more on PyDub's doc.
    """
    def get_file_extension(filename):
        """A helper function to get a file's extension"""
        return os.path.splitext(filename)[1].lstrip(".")

    clips = []
    # wrap the audio clip paths with tqdm if verbose
    audio_clip_paths = tqdm(audio_clip_paths, "Reading audio file") if verbose else audio_clip_paths
    for clip_path in audio_clip_paths:
        # get extension of the audio file
        extension = get_file_extension(clip_path)
        # load the audio clip and append it to our list
        clip = AudioSegment.from_file(clip_path, extension)
        clips.append(clip)

    final_clip = clips[0]
    range_loop = tqdm(list(range(1, len(clips))), "Concatenating audio") if verbose else range(1, len(clips))
    for i in range_loop:
        # looping on all audio files and concatenating them together
        # ofc order is important
        final_clip = final_clip + clips[i]
    # export the final clip
    final_clip_extension = get_file_extension(output_path)
    if verbose:
        print(f"Exporting resulting audio file to {output_path}")
    final_clip.export(output_path, format=final_clip_extension)

instructions = 50
files = [f"{mypath}/Start.mp3"]
for x in range(0, instructions):
    attackrand = random.randint(0, len(attack)-1)
    chosen_attack = attack[attackrand]
    defenserand = random.randint(0, len(defense)-1)
    chosen_defense = defense[defenserand]
    print(f"{attack[attackrand]}, then {defense[defenserand]}")
    files.append(f"{mypath}/{chosen_attack}.mp3")
    files.append(f"{mypath}/{silence[0]}.mp3")
    files.append(f"{mypath}/{chosen_defense}.mp3")
    files.append(f"{mypath}/{silence[1]}.mp3")


files.append(f"{mypath}/Stop.mp3")

concatenate_audio_pydub(files, "mash2.mp3")
