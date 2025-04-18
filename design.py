import streamlit as st

def set_page_config():
    st.set_page_config(page_title="Voice-to-Text AI", layout="centered")

def custom_styling():
    # Custom CSS styles
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
                padding: 10px;
                border-radius: 8px;
                border: 1px solid #ccc;
                background-color: #f9f9f9;
            }
        </style>
    """, unsafe_allow_html=True)

def display_title():
    # Updated title and description for the app
    st.markdown("<h1 style='text-align:center; color:#0078D4;'>🎙️ Transform Your Audio to Text with AI</h1>", unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align:center; font-size:18px; color:#333;">
            Upload an audio file and instantly receive an AI-generated transcript powered by Whisper.<br>
            Perfect for meetings, interviews, podcasts, and more!
        </div>
    """, unsafe_allow_html=True)
