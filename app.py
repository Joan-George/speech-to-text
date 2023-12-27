import streamlit as st
from streamlit_speech_to_text import speech_to_text

v_custom = speech_to_text()

st.text_area(
    label="Transcription",
    value=v_custom,
    disabled=True,
    key='transcription',
)
st.write(v_custom)
