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




API_URL = "https://ry8lw5hyfuiiv805.us-east-1.aws.endpoints.huggingface.cloud"
API_TOKEN = "2gW0BQPEIHuZxNYGYZsmYNzRXXI_4hiDxccm7aMjMZPn8LLA6" 

import streamlit as st
import pandas as pd
import requests
import locale
from statistics import mean
from evaluate import load

# Load your dataframe
data = pd.read_csv('sample_news.csv')


headers = {"Authorization": f"Bearer {API_TOKEN}"}

locale.getpreferredencoding = lambda: "UTF-8"

def summarize_text(text):
    payload = {"inputs": text.strip()}
    response = requests.post(API_URL, json=payload, headers=headers)
    return response.json()

def calc_rouges(rouge_scores, rouge_type):
    rouge_h = rouge_scores[rouge_type].high.fmeasure
    rouge_m = rouge_scores[rouge_type].mid.fmeasure
    rouge_l = rouge_scores[rouge_type].low.fmeasure
    return mean([rouge_h, rouge_m, rouge_l])

def evaluate_summary(candidate, reference, bleu_metric, rouge_metric, bertscore_metric):
    # Compute BLEU score
    bleu_scores = bleu_metric.compute(predictions=[candidate], references=[reference])
    bleu = bleu_scores['precisions'][0]

    # Compute ROUGE score
    rouge_scores = rouge_metric.compute(predictions=[candidate], references=[reference])
    rouge1 = calc_rouges(rouge_scores, 'rouge1')
    rouge2 = calc_rouges(rouge_scores, 'rouge2')
    rougeL = calc_rouges(rouge_scores, 'rougeL')

    # Compute BERTScore
    bertscore_results = bertscore_metric.compute(predictions=[candidate], references=[reference], lang="en")
    b_prec = mean(bertscore_results['precision'])
    b_rec = mean(bertscore_results['recall'])
    b_f1 = mean(bertscore_results['f1'])

    return bleu, rouge1, rouge2, rougeL, b_prec, b_rec, b_f1

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
            # Load metrics after the checkbox is checked
            bleu_metric = load('bleu')
            rouge_metric = load('rouge')
            bertscore_metric = load('bertscore')
            
            # Calculate and display metrics
            bleu, rouge1, rouge2, rougeL, b_prec, b_rec, b_f1 = evaluate_summary(summary, human_summary, bleu_metric, rouge_metric, bertscore_metric)
            st.metric("BLEU Score", f"{bleu:.2f}")
            st.metric("ROUGE-1 Score", f"{rouge1:.2f}")
            st.metric("ROUGE-2 Score", f"{rouge2:.2f}")
            st.metric("ROUGE-L Score", f"{rougeL:.2f}")
            st.metric("BERT Precision", f"{b_prec:.2f}")
            st.metric("BERT Recall", f"{b_rec:.2f}")
            st.metric("BERT F1 Score", f"{b_f1:.2f}")

if __name__ == "__main__":
    main()
