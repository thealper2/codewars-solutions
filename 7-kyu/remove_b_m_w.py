import re


def remove_bmw(s):
    if not isinstance(s, str):
        raise TypeError('This program only works for text.') 
    
    return re.sub(r'(?i)[bmw]', '', s)
