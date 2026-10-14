import re

def camelize(str_):
    words = re.split(r'[^A-Za-z0-9]+', str_)
    return ''.join(word.capitalize() for word in words if word)