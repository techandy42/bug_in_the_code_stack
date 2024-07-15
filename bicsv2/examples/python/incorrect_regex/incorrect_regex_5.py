import re

def extract_html_tags(html):
    pattern = re.compile(r"<[^>]+")
    return pattern.findall(html)
