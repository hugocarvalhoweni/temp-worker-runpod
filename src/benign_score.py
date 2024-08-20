from probabilities import get_class_probabilities

def get_indirect_injection_score(text, temperature=1.0, device='cpu'):
    """
    Evaluate the probability that a given string contains any embedded instructions (malicious or benign).
    Appropriate for filtering third party inputs (e.g. web searches, tool outputs) into an LLM.

    Args:
        text (str): The input text to evaluate.
        temperature (float): The temperature for the softmax function. Default is 1.0.
        device (str): The device to evaluate the model on.

    Returns:
        float: The combined probability of the text containing malicious or embedded instructions.
    """
    probabilities = get_class_probabilities(text, temperature, device)
    return (probabilities[0, 1] + probabilities[0, 2]).item()