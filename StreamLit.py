import streamlit as st

st.title("Hi Lauren!")

st.write('Daniel is working on this')
st.text_input('Source airport:')

st.write("Text input in columns:")
buff, col, buff2 = st.columns([1, 3, 1])
col.text_input('Smaller text window:')
