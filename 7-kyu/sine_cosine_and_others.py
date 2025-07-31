import math


def sctc(sin):
    if not -1 <= sin <= 1:
        return []

    result = [round(sin, 2)]

    try:
        cos = math.sqrt(1 - sin**2)
        result.append(round(cos, 2))
    except:
        return result

    try:
        tan = sin / cos
        result.append(round(tan, 2))
    except ZeroDivisionError:
        pass

    try:
        cot = cos / sin
        result.append(round(cot, 2))
    except ZeroDivisionError:
        pass

    return result
