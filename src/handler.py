import runpod
from jailbreak_score import get_jailbreak_score

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