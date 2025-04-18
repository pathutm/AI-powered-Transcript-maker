import streamlit as st
import whisper
import tempfile
import os
from pydub.utils import mediainfo

@st.cache_resource
def load_model():
    return whisper.load_model("base")

def transcribe_audio(file_path, model):
    try:
        return model.transcribe(file_path)
    except Exception as e:
        raise ValueError(f"Error during transcription: {str(e)}")

def save_uploaded_file(uploaded_file):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
            tmp_file.write(uploaded_file.read())
            return tmp_file.name
    except Exception as e:
        raise ValueError(f"Error saving file: {str(e)}")

def get_audio_duration(file_path):
    try:
        info = mediainfo(file_path)
        return float(info["duration"])
    except Exception as e:
        raise ValueError(f"Error getting duration: {str(e)}")
