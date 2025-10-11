def convert(st): 
    if not st:
        return 0
    
    st = st.upper()
    if len(st) == 1:
        return 1
    
    mapping = {}
    digits_used = 0
    available_digits = list(range(10))
    
    for char in st:
        if char not in mapping:
            if len(mapping) == 0:
                mapping[char] = 1
                available_digits.remove(1)
                digits_used += 1
            else:
                if 0 in available_digits and len(mapping) == 1:
                    mapping[char] = 0
                    available_digits.remove(0)
                else:
                    mapping[char] = available_digits[0]
                    available_digits = available_digits[1:]
                digits_used += 1
    
    result_str = ''.join(str(mapping[char]) for char in st)
    return int(result_str)
