import streamlit as st
from streamlit_speech_to_text import speech_to_text

def initialize_app():
    if 'mycall_output' not in st.session_state:
        st.session_state.mycall_output = ''

def mycall():
    st.session_state.mycall_output = f"mycall__{st.session_state.react_stt_output}"
    # st.experimental_rerun()

def voice_transcriber():
    initialize_app()
    v_custom = speech_to_text(callback = mycall, key = 'react_stt')

    st.text_area(
        label="Transcription",
        value=v_custom,
        disabled=True,
        key='transcription',
    )
    st.write(f"{v_custom}{type(v_custom)}")
    st.write(f"output of callback:{st.session_state.mycall_output}")



if __name__ == '__main__':
    voice_transcriber()