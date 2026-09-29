def rev_rot(s, sz):
    if sz <= 0 or s == "" or sz > len(s):
        return ""
    
    result = []
    for i in range(0, len(s) - sz + 1, sz):
        chunk = s[i:i + sz]
        digit_sum = sum(int(c) for c in chunk)
        if digit_sum % 2 == 0:
            result.append(chunk[::-1])
        else:
            result.append(chunk[1:] + chunk[0])
            
    return ''.join(result)