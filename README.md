# News Summarizer using Llama2 Qlora

This is a News Summarizer application built using Llama2 Qlora. It summarizes news articles to provide concise and informative summaries.

## Finetuned Huggingface Card


<img src="images/huggingface_card.png" width="400" />

You can access the News Summarizer Model [here](https://huggingface.co/YasaminAbb/Llama-2-7b-CNN_Q_lora_Summarizer/tree/main).

## Preview of Streamlit App

<img src="images/url_address.png" width="300" />
<p float="left">
  <img src="images/news_app_snap1.png" width="300" />
  <img src="images/news_app_snap2.png" width="500" /> 
</p>



## Access the Azure Deployed Streamlit App

You can access the News Summarizer app [here](https://newssummarizer.azurewebsites.net/).
## 
🚨 **Instance Deactivation Notice** 🚨

🔴 **Attention:** 

The instances for the app have been **deactivated temporarily**. 

⚠️ **What does this mean?** 

Access to the application is currently **unavailable**. 
🔒 **Why?**
To conserve resources and optimize performance, we've paused the instances. 
🔓 **What should I do?**
If you need to activate the instances or have any queries, please **reach out** to us. 

Thank you for your understanding and cooperation! 🙏

## Endpoint Specifications

### Hugging Face API and AWS Endpoint for Model Inference

This repository uses the Hugging Face API and an AWS endpoint for model inference. The API is deployed on an AWS instance with the following specifications:

#### Hardware Specifications

* **GPU**: Nvidia T4
* **Number of GPUs**: 1
* **Memory**: 16 GB

This setup enables fast and efficient model inference.

### Azure Endpoint for Streamlit UI

The Streamlit UI is hosted on an Azure endpoint with the following specifications:

#### Pricing and Hardware Specifications

* **Pricing**: Basic B1 ($13.14 USD/Month)
* **ACU**: 100
* **Memory**: 1.75 GB
* **vCPU**: 1

This setup provides a reliable and cost-effective way to host the Streamlit UI.



## model_api_inference
### handler.py

- A handler in Hugging Face helps manage API endpoints.
- It acts like a middleman between incoming requests and the model.
- When someone sends a request to the API, the handler processes it.
- It sends the data to the model for prediction.
- Then, it formats the model's response before sending it back.
So, handlers are crucial for making sure the API works smoothly and interacts correctly with the deployed model.



## Contributors

- Yasamin Abbaszadegan
