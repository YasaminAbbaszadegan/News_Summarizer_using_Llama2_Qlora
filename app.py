# import streamlit as st
# import requests

# # API_URL = ""
# # API_TOKEN = ""
# API_URL = "https://ry8lw5hyfuiiv805.us-east-1.aws.endpoints.huggingface.cloud"
# API_TOKEN = "2gW0BQPEIHuZxNYGYZsmYNzRXXI_4hiDxccm7aMjMZPn8LLA6" 

# headers = {"Authorization": f"Bearer {API_TOKEN}"}

# def summarize_text(text):
#     payload = {"inputs": text.strip()}
#     response = requests.post(API_URL, json=payload, headers=headers)
#     return response.json()

# def main():
#     st.title("Text Summarization App")
    
#     # Define a text area for user input
#     text_input = st.text_area("Enter the text to summarize", height=300)


#     # Add a button to trigger the summarization
#     if st.button("Summarize"):
#         # Display a spinner while summarization is in progress
#         with st.spinner("Summarizing..."):
#             # Call summarize_text function with user input
#             summary = summarize_text(text_input)
        
#         # Display the summarized text in a print-like format
#         st.subheader("Summary")
#         st.markdown(f"```\n{summary}\n```")
# if __name__ == "__main__":
#     main()



import streamlit as st
import pandas as pd
import requests
# import locale
# from statistics import mean
# from evaluate import load




API_URL = "https://ry8lw5hyfuiiv805.us-east-1.aws.endpoints.huggingface.cloud"
API_TOKEN = "2gW0BQPEIHuZxNYGYZsmYNzRXXI_4hiDxccm7aMjMZPn8LLA6" 

# Load your dataframe
data = pd.read_csv('sample_news.csv')


headers = {"Authorization": f"Bearer {API_TOKEN}"}

# locale.getpreferredencoding = lambda: "UTF-8"

def summarize_text(text):
    payload = {"inputs": text.strip()}
    response = requests.post(API_URL, json=payload, headers=headers)
    return response.json()

def main():
    st.title("Text Summarization App")
    
    # Option to select from dataframe
    use_dataframe = st.checkbox("Use dialogue from dataframe")
    
    text_input = ""
    human_summary = ""
    
    if use_dataframe:
        dialogue_options = data['dialogue'].tolist()
        selected_dialogue = st.selectbox("Select a dialogue", dialogue_options)
        text_input = selected_dialogue
        # Get the corresponding human summary
        human_summary = data[data['dialogue'] == selected_dialogue]['summary'].values[0]
        # Display the selected dialogue in a large text box
        st.text_area("Selected Dialogue", value=selected_dialogue, height=300, disabled=True)
        
        
    else:
        # Define a text area for user input
        text_input = st.text_area("Enter the text to summarize", height=300)

    # Add a button to trigger the summarization
    if st.button("Summarize"):
        # Display a spinner while summarization is in progress
        with st.spinner("Summarizing..."):
            # Call summarize_text function with user input
            summary = summarize_text(text_input)
        
        # Display the summarized text in a print-like format
        st.subheader("Generative Summary")
        st.markdown(f"```\n{summary}\n```")
        
        if use_dataframe:
            # Display the human summary
            st.subheader("Human Summary")
            st.markdown(f"```\n{human_summary}\n```")

if __name__ == "__main__":
    main()


