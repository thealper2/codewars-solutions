import math


def graceful_tipping(bill):
    tip = bill * 0.15
    total = bill + tip
    
    if total < 10:
        return math.ceil(total)
    else:
        magnitude = 10 ** (math.floor(math.log10(total)))
        divisor = 5 * (magnitude // 10)
        rounded = math.ceil(total / divisor) * divisor
        return int(rounded)
