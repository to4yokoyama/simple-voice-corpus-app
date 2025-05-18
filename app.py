import streamlit as st
import pandas as pd
import os
import shutil
import subprocess
from audiorecorder import audiorecorder
from pydub import AudioSegment

def save_trimmed_wav_cut1sec(audio, filepath):
    cut_ms = 1000 

    if len(audio) > cut_ms:
        trimmed = audio[cut_ms:]
    else:
        trimmed = audio 

    trimmed.export(filepath, format="wav")
def cut_wav_start_ffmpeg(input_path, cut_seconds=1.0):
    temp_path = input_path.replace(".wav", "_tmp.wav")

    cmd = [
        "ffmpeg",
        "-y",
        "-i", input_path,
        "-af", "agate=threshold=0.05",
        "-ar", "48000",
        "-ac", "1",
        "-acodec", "pcm_s16le",
        temp_path
    ]

    subprocess.run(cmd, check=True)
    shutil.move(temp_path, input_path)


# Title
st.title("Corpus Recorder")

# Prepare output directory
os.makedirs("wavs", exist_ok=True)

# Load metadata.csv (with "author" column)
df = pd.read_csv("metadata.csv", sep="|", header=None, names=["filename", "author", "lang", "text"])

# Show recording UI per row
for idx, row in df.iterrows():
    st.markdown(f"### 📝 {row['text']}")

    audio = audiorecorder(f"▶️ Start recording [{row['filename']}]", "■ Stop")

    filepath = os.path.join("wavs", row["filename"])

    # Audio playback placeholder
    audio_player = st.empty()

    if os.path.exists(filepath):
        audio_player.audio(filepath, format="audio/wav")

    if len(audio) > 0:
        segment = AudioSegment(
            data=audio.raw_data,
            sample_width=audio.sample_width,
            frame_rate=audio.frame_rate,
            channels=1
        )

        save_trimmed_wav_cut1sec(segment, filepath) 
        cut_wav_start_ffmpeg(filepath, cut_seconds=0.0)
        audio_player.audio(filepath, format="audio/wav")
