import re

def extract_floats(text):
    pattern = re.compile(r"\b\d+.\d+\b")
    return pattern.findall(text)
