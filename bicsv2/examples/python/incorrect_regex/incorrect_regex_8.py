import re

def extract_sentences(text):
    pattern = re.compile(r"\w+[.!?]")
    return pattern.findall(text)
