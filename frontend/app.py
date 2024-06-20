import streamlit as st

st.title("Internal Knowledge Base Search")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.write("File uploaded successfully!")
