import re

def is_vowel(s):
    return bool(re.fullmatch(r'(?i)[aeiou]', s))
