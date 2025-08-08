import math


def to_scientific(num):
    if num < 1000:
        return str(num)

    exponent = int(math.log10(num))
    mantissa = num / (10 ** exponent)
    mantissa = math.floor(mantissa * 1000) / 1000
    mantissa_str = f"{mantissa:.3f}".rstrip('0').rstrip('.')
    if '.' not in mantissa_str:
        mantissa_str += '.0'

    return f"{mantissa_str}e{exponent}"
