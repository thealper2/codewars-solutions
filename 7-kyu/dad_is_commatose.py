import re

def dad_filter(text):
    text = re.sub(r',+', ',', text)
    text = text.strip()
    text = text if text[-1] != ',' else text[:-1]
    return text