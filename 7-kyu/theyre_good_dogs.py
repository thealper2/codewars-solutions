import re

def we_rate_dogs(s, rating):
    return re.sub(r'\d+/10', f'{rating}/10', s, count=1)
