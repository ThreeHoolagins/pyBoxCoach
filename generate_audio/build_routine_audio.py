from tqdm import tqdm
from pydub import AudioSegment
from boxing_move import BoxingMove
from pydub.utils import which
import os

from constants import BoxingMovesConstants, FileLocationConstants

AudioSegment.converter = which("ffmpeg")

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

def build_instruction_set_audio(routine, has_padding=False):
    
    instruction_files = []
    for instruction in routine:
        if type(instruction) is BoxingMove:
            instruction_files.append(f"{FileLocationConstants.AUDIO_SRC_PATH}/{instruction.move}.mp3")
        else:
            instruction_files.append(f"{FileLocationConstants.AUDIO_SRC_PATH}/{instruction}.mp3")
            
        if has_padding:
            instruction_files.append(f"{FileLocationConstants.AUDIO_SRC_PATH}/{BoxingMovesConstants.SILENCE_OPTIONS[1]}.mp3")

    concatenate_audio_pydub(instruction_files, "./output/routine.mp3")