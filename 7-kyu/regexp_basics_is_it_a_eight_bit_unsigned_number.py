import re


def eight_bit_number(n):
    return bool(re.fullmatch(r'0|([1-9]\d?|1\d{2}|2[0-4]\d|25[0-5])', n))
