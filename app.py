import streamlit as st
from whisper_model import load_model, transcribe_audio, save_uploaded_file, get_audio_duration
import os

# Page settings
st.set_page_config(page_title="Voice-to-Text AI", layout="centered")

# Custom styles
st.markdown("""
    <style>
        .stButton>button {
            background-color: #0078D4;
            color: white;
            font-weight: bold;
            border-radius: 12px;
            padding: 10px 20px;
            transition: background-color 0.3s;
        }
        .stButton>button:hover {
            background-color: #005A9E;
        }
        .stTextArea textarea {
            font-family: 'Arial', sans-serif;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align:center;'>🎙️ Audio to Text Transcription</h1>", unsafe_allow_html=True)
st.markdown("Upload an audio file and get an AI-generated transcript using **Whisper**.")

# Load model
model = load_model()

# Upload audio
uploaded_file = st.file_uploader("Upload an audio file (mp3, m4a, wav, etc.)", type=["mp3", "m4a", "wav", "webm", "mp4"])

if uploaded_file:
    st.audio(uploaded_file, format='audio/mpeg')
    st.info(f"📁 File name: `{uploaded_file.name}`\n\n📦 Size: {round(uploaded_file.size / 1024, 2)} KB")

    # Save audio
    temp_path = save_uploaded_file(uploaded_file)

    # Show duration
    try:
        audio_duration = get_audio_duration(temp_path)
        st.info(f"🎧 Audio Duration: {audio_duration:.2f} seconds")
    except Exception as e:
        st.warning(f"⚠️ Could not determine duration: {e}")

    # File size check
    if uploaded_file.size > 200 * 1024 * 1024:
        st.warning("⚠️ The file is too large. Please upload a file under 50 MB.")
    else:
        with st.spinner("🧠 Transcribing... Please wait."):
            try:
                result = transcribe_audio(temp_path, model)
                st.success("✅ Transcription Complete!")
                st.text_area("📝 Transcribed Text", value=result["text"], height=300)
                st.download_button("⬇️ Download Transcript", result["text"], file_name="transcript.txt")
            except Exception as e:
                st.error(f"❌ Error during transcription: {e}")

    # Delete temp file
    os.remove(temp_path)

# At the bottom of your app.py
if st.button("Clear All"):
    st.markdown("""
        <meta http-equiv="refresh" content="0">
    """, unsafe_allow_html=True)

