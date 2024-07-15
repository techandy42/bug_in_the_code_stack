import re

def extract_filenames(text, extensions):
    pattern = re.compile(r"\b\w+(\.?:" + "|".join(extensions) + r")\b")
    return pattern.findall(text)
