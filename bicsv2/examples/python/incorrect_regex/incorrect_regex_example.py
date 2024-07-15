import re

def extract_hashtags(text):
    pattern = re.compile(r"@\w+")
    return pattern.findall(text)
