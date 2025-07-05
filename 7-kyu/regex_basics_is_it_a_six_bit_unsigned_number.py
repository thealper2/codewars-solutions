import re


def six_bit_number(n):
    return bool(re.fullmatch(r'(0|[1-5]?\d|6[0-3])', n))
