import re


def valid_phone_number(phone_number):
    return bool(re.fullmatch(r'\(\d{3}\) \d{3}-\d{4}', phone_number))