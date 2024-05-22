from typing import Any, Dict
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftConfig, PeftModel

class EndpointHandler:
    """
    Custom handler for processing inference requests.
    """

    def __init__(self, path: str = "") -> None:
        """
        Initialize the endpoint handler.

        Args:
            path (str): Path to the model repository.
        """
        # Determine the data type based on the CUDA device capability
        dtype = torch.bfloat16 if torch.cuda.get_device_capability()[0] == 8 else torch.float16

        # Configure BitsAndBytes quantization
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=dtype
        )

        # Load model configuration and tokenizer
        config = PeftConfig.from_pretrained(path)
        model = AutoModelForCausalLM.from_pretrained(
            config.base_model_name_or_path,
            return_dict=True,
            quantization_config=bnb_config,
            device_map="auto",
            torch_dtype=dtype,
            trust_remote_code=True,
        )
        tokenizer = AutoTokenizer.from_pretrained(config.base_model_name_or_path)
        tokenizer.pad_token = tokenizer.eos_token
        self.tokenizer = tokenizer

        # Initialize the model with PeftModel
        self.model = PeftModel.from_pretrained(model, path)

    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process an inference request.

        Args:
            data (Dict[str, Any]): Input data dictionary.

        Returns:
            Dict[str, Any]: Output data dictionary.
        """
        # Extract input prompt from data
        prompt = data.pop("inputs", data)
        
        # Prepare input prompt for summarization
        prompt = f"""
        ### Instruction:
        Summarize the following News Article.
        ​
        ### Input:
        {prompt}
        ​
        ### Summary:
        """.strip()
        
        # Tokenize input prompt
        input_ids = self.tokenizer(prompt, return_tensors='pt', truncation=True).input_ids.cuda()
        
        # Generate summary
        outputs = self.model.generate(input_ids=input_ids, max_new_tokens=200)
        output = self.tokenizer.batch_decode(outputs.detach().cpu().numpy(), skip_special_tokens=True)[0][len(prompt):]
        
        return output



"""
Class Definition: The EndpointHandler class is defined, serving as a custom handler for processing inference requests.

Initialization Method: 
The __init__ method initializes the handler. It loads the model configuration and tokenizer, configures BitsAndBytes quantization, and initializes the model with PeftModel.

Call Method: 

The __call__ method processes an inference request.

It extracts the input prompt from the data dictionary, prepares it for summarization, tokenizes it, generates a summary using the model, and returns the output summary.
"""