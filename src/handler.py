import runpod
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from huggingface_hub import login
from jailbreak_score import get_jailbreak_score
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
)
import os

load_dotenv()

login(token=f"{os.getenv('HUGGING_FACE_ACCESS_TOKEN')}")

prompt_injection_model_name = 'meta-llama/Prompt-Guard-86M'
tokenizer = AutoTokenizer.from_pretrained(prompt_injection_model_name)
model = AutoModelForSequenceClassification.from_pretrained(prompt_injection_model_name)

def handler(job):
    job_input = job['input']

    inference = round(get_jailbreak_score(job_input), 2)

    if inference >= 0.7:
        inference_classification = "Injection"
    else:
        inference_classification = "Benign"

    classification = {
        "guardrails_classification": inference_classification
    }

    return classification


runpod.serverless.start({"handler": handler})