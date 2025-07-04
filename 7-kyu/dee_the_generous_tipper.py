import math


def calc_tip(price, satisfaction):
    units_digit = price % 10
    if units_digit >= 5:
        rounded_price = math.ceil(price / 10) * 10
    else:
        rounded_price = math.floor(price / 10) * 10
    
    base_tip = rounded_price // 10

    if satisfaction == 1:
        adjusted_tip = base_tip + 1
    elif satisfaction == 0:
        adjusted_tip = base_tip - 1
    elif satisfaction == -1:
        adjusted_tip = (base_tip // 2) - 1
    else:
        adjusted_tip = 0
    
    adjusted_tip = max(adjusted_tip, 0)
    return adjusted_tip
