import re


def timed_reading(max_length, text):
    words = re.findall(r"[a-zA-Z]+", text)
    return sum(1 for word in words if len(word) <= max_length)
