import streamlit as st
import requests

st.title("Internal Knowledge Base Search")

# File upload component
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file is not None:
    # Display the uploaded file
    st.write("File uploaded:", uploaded_file.name)

# Search bar component
query = st.text_input("Enter your search query")

if query:
    # Perform the search
    response = requests.post("http://backend_api/search", json={"query": query})
    results = response.json()

    # Display the search results
    for result in results:
        st.write(result["title"])
        st.write(result["snippet"])
        st.write(result["url"])
