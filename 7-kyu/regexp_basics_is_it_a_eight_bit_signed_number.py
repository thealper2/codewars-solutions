import re


def signed_eight_bit_number(number):
    pattern = (
        r"^(0|[1-9][0-9]?|1[01][0-9]|12[0-7]|-([1-9]|[1-9][0-9]|1[01][0-9]|12[0-8]))$"
    )
    return bool(re.fullmatch(pattern, number))
