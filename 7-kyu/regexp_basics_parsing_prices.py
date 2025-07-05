import re


def to_cents(amount):
    matches = re.fullmatch(r'\$(\d+)\.(\d{2})', amount)
    if matches:
        dollars = int(matches.group(1))
        cents = int(matches.group(2))
        return dollars * 100 + cents
    
    return None