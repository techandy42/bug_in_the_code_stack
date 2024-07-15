import re

def validate_hex_colors(color_list):
    valid_colors = []
    pattern = re.compile(r"#[0-9]{6}\b")
    for color in color_list:
        if pattern.match(color):
            valid_colors.append(color)
    return valid_colors
