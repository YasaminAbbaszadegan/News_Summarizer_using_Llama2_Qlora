import streamlit as st
import requests

API_URL = "https://ry8lw5hyfuiiv805.us-east-1.aws.endpoints.huggingface.cloud"
API_TOKEN = "2gW0BQPEIHuZxNYGYZsmYNzRXXI_4hiDxccm7aMjMZPn8LLA6"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def summarize_text(text):
    payload = {"inputs": text.strip()}
    response = requests.post(API_URL, json=payload, headers=headers)
    return response.json()

def main():
    st.title("Text Summarization App")
    
    # Define a text area for user input
    text_input = st.text_area("Enter the text to summarize", height=300)


    # Add a button to trigger the summarization
    if st.button("Summarize"):
        # Display a spinner while summarization is in progress
        with st.spinner("Summarizing..."):
            # Call summarize_text function with user input
            summary = summarize_text(text_input)
        
        # Display the summarized text in a print-like format
        st.subheader("Summary")
        st.markdown(f"```\n{summary}\n```")
if __name__ == "__main__":
    main()
