def add(a, b):
    a_str = str(a)
    b_str = str(b)
    max_len = max(len(a_str), len(b_str))
    a_str = a_str.zfill(max_len)
    b_str = b_str.zfill(max_len)
    result = ''
    
    for i in range(max_len):
        digit_sum = int(a_str[i] ) + int(b_str[i])
        result += str(digit_sum)
        
    return int(result)
