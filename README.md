# News Summarizer Application

This is a News Summarizer application built using Llama2 QLoRA. It summarizes news articles to provide concise and informative summaries.

## Features

- **Fine-Tuned LLMs (LLaMA2):** The model has been fine-tuned on a news dataset, optimizing computational resources by training with only 20% of the original parameters using QLoRA. This approach achieves an impressive 80% average BERTScore, ensuring high-quality summaries.
- **Deployment:** The fine-tuned LLM model is deployed using HuggingFace Inference Endpoint REST APIs. Additionally, a user-friendly interface has been developed using Streamlit, enhancing user interaction and accessibility.
- **Automated MLOps Workflow:** The application leverages Azure Web Apps and GitHub to automate the MLOps workflow. This setup streamlines the CI/CD pipeline, ensuring efficient model deployment and continuous monitoring.
  
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
If you need to activate the instances or have any queries, please **reach out** to me. 

Thank you for your understanding and cooperation! 🙏

## Endpoint Resource Specifications

### Hugging Face API and AWS Endpoint for Model Inference

This repository uses the Hugging Face API and an AWS endpoint for model inference. The API is deployed on an AWS instance with the following specifications:

####  🎮 / 🧠  Hardware Specifications

* **GPU**: Nvidia T4 ($0.5 USD/Hour)
* **Number of GPUs**: 1 
* **Memory**: 16 GB

This setup enables fast and efficient model inference.

###  Azure Endpoint for Streamlit UI

The Streamlit UI is hosted on an Azure endpoint with the following specifications:

#### 🎮 / 🧠  Hardware Specifications

* **Pricing**: Basic B1 ($13.14 USD/Month)
* **ACU**: 100
* **Memory**: 1.75 GB
* **vCPU**: 1

This setup provides a reliable and cost-effective way to host the Streamlit UI.

## Finetuning Colab Resource Specifications
#### 🎮 / 🧠  Hardware Specifications
* **GPU**: Nvidia L4
* **Number of GPUs**: 1
* **Memory**: 24GB of VRAM!

## model_api_inference
### handler.py

- A handler in Hugging Face helps manage API endpoints.
- It acts like a middleman between incoming requests and the model.
- When someone sends a request to the API, the handler processes it.
- It sends the data to the model for prediction.
- Then, it formats the model's response before sending it back.
So, handlers are crucial for making sure the API works smoothly and interacts correctly with the deployed model.


## Reference Resources
### Optimizing LLMs
[Optimizing LLMs: A Step-by-Step Guide to Fine-Tuning with PEFT and QLoRa](https://medium.com/etoai/optimizing-llms-a-step-by-step-guide-to-fine-tuning-with-peft-and-qlora-22eddd13d25b![image](https://github.com/YasaminAbbaszadegan/News_Summarizer_using_Llama2_Qlora/assets/51804165/998ddf0b-ef07-488d-971c-b8a9c8d85960)
)
### Deploy LLM to Production
[Deploy LLM to Production with HuggingFace Inference Endpoints](https://www.mlexpert.io/blog/deploy-llm-to-production#merge-qlora-adapter-with-base-model![image](https://github.com/YasaminAbbaszadegan/News_Summarizer_using_Llama2_Qlora/assets/51804165/459fdd51-2f6b-4b3c-9314-2a018a34fdcb)
)
Let me know if you have any other requests!



## Contributors

- Yasamin Abbaszadegan
