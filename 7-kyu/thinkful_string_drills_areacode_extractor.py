import re


def area_code(text):
    match = re.search(r'\((\d{3})\)', text)
    if match:
        return match.group(1)
    
    return None
