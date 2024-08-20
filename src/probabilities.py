from torch.nn.functional import softmax
from builder.model_setup import model, tokenizer
import torch

def get_class_probabilities(text, temperature=1.0, device='cpu'):
    """
    Evaluate the model on the given text with temperature-adjusted softmax.

    Args:
        text (str): The input text to classify.
        temperature (float): The temperature for the softmax function. Default is 1.0.
        device (str): The device to evaluate the model on.

    Returns:
        torch.Tensor: The probability of each class adjusted by the temperature.
    """
    # Encode the text
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    inputs = inputs.to(device)
    # Get logits from the model
    with torch.no_grad():
        logits = model(**inputs).logits
    # Apply temperature scaling
    scaled_logits = logits / temperature
    # Apply softmax to get probabilities
    probabilities = softmax(scaled_logits, dim=-1)
    return probabilities