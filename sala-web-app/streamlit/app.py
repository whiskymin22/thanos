import streamlit as st
import requests

st.title("Excel File Upload")

st.write("Upload your Excel file to process it.")

uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])

if uploaded_file is not None:
    # Display the file details
    st.write("Filename:", uploaded_file.name)
    st.write("File size:", uploaded_file.size, "bytes")

    # Send the file to the FastAPI backend for processing
    response = requests.post("http://backend:8000/api/upload", files={"file": uploaded_file})

    if response.status_code == 200:
        st.success("File uploaded and processed successfully!")
        st.write(response.json())  # Display the response from the backend
    else:
        st.error("Error uploading file: " + response.text)