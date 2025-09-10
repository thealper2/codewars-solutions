import re


def body_count(code):
    pattern = r'[A-Z]\d[A-Z]\d[A-Z]\d[A-Z]\d[A-Z]\d\.\-[A-Z]%\d\.\d\d\.'
    return bool(re.search(pattern, code))
