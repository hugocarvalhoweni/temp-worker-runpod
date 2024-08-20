from probabilities import get_class_probabilities

def get_jailbreak_score(text, temperature=1.0, device='cpu'):
    """
    Evaluate the probability that a given string contains malicious jailbreak or prompt injection.
    Appropriate for filtering dialogue between a user and an LLM.

    Args:
        text (str): The input text to evaluate.
        temperature (float): The temperature for the softmax function. Default is 1.0.
        device (str): The device to evaluate the model on.

    Returns:
        float: The probability of the text containing malicious content.
    """
    probabilities = get_class_probabilities(text, temperature, device)
    return probabilities[0, 2].item()