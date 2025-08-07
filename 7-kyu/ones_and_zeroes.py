def same_length(s):
    if not s or s[0] == '0':
        return False
    
    count_ones = s.count('1')
    count_zeros = s.count('0')
    if count_ones != count_zeros:
        return False
    
    i = 0
    n = len(s)
    while i < n:
        if s[i] == '1':
            ones_length = 0
            while i < n and s[i] == '1':
                ones_length += 1
                i += 1
            zeros_length = 0
            while i < n and s[i] == '0':
                zeros_length += 1
                i += 1
            if ones_length != zeros_length:
                return False
        else:
            return False
        
    return True
