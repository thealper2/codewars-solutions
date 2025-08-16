import re

def coffee(text):
    return re.sub(r'\bcoffee\b', 'COFFEE', text, flags=re.IGNORECASE)
