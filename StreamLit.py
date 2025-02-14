import streamlit as st

st.title("Hi Lauren!")

st.write('A standard text input:')
st.text_input('Write some text here:')

st.write("Text input in columns:")
buff, col, buff2 = st.columns([1, 3, 1])
col.text_input('Smaller text window:')
