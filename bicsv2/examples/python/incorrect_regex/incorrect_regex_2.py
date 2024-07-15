import re

def extract_phone_numbers(text):
    pattern = re.compile(r"\b\d{4}[-.\s]?\d{3}[-.\s]?\d{3}\b")
    return pattern.findall(text)
