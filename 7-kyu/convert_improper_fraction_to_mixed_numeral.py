def convert_to_mixed_numeral(parm):
    parts = parm.split('/')
    numerator = int(parts[0])
    denominator = int(parts[1])
    
    sign = 1
    if numerator < 0:
        sign = -1
        numerator = -numerator
    if denominator < 0:
        sign *= -1
        denominator = -denominator
    
    if numerator < denominator:
        if sign == -1:
            return f'-{numerator}/{denominator}'
        else:
            return f'{numerator}/{denominator}'
    
    whole_number = numerator // denominator
    remainder = numerator % denominator
    whole_number *= sign
    
    if remainder == 0:
        return f'{whole_number}'
    else:
        if whole_number == 0:
            return f'{remainder}/{denominator}'
        else:
            return f'{whole_number} {remainder}/{denominator}'
