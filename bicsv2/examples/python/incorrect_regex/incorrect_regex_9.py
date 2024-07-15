import re

def extract_capitalized_words(text):
    pattern = re.compile(r"\b[a-z][a-z]*\b")
    return pattern.findall(text)
