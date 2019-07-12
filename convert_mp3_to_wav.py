import tempfile
import os, shutil
import pydub
import scipy
from scipy.io import wavfile


MP3_AUDIO_DIR = "AllAudio/"
WAV_AUDIO_DIR = "AllAudioWav/"



def read_mp3(file_path):
  

    path, ext = os.path.splitext(file_path)
    assert ext=='.mp3'
    mp3 = pydub.AudioSegment.from_mp3(file_path)
    _, path = tempfile.mkstemp()
    mp3.export(path, format="wav")
    os.close(_)
    return path

if len(list(os.listdir(WAV_AUDIO_DIR))) == 0:
    for f in os.listdir(MP3_AUDIO_DIR):
        shutil.copy2(read_mp3(MP3_AUDIO_DIR+f),WAV_AUDIO_DIR)





