import re

def autocorrect(text):
    return re.sub(r'\byouu*\b|\bu\b', 'your sister', text, flags=re.IGNORECASE)