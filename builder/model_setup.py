from transformers import AutoTokenizer, AutoModelForSequenceClassification
from dotenv import load_dotenv
from huggingface_hub import login
import os

load_dotenv()

login(token=f"{os.getenv('HUGGING_FACE_ACCESS_TOKEN')}")

prompt_injection_model_name = 'meta-llama/Prompt-Guard-86M'
tokenizer = AutoTokenizer.from_pretrained(prompt_injection_model_name)
model = AutoModelForSequenceClassification.from_pretrained(prompt_injection_model_name)