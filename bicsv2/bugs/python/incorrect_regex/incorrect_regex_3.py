import re

def find_urls(text):
    pattern = re.compile(r"https?:///[^\s]+")
    return pattern.findall(text)
