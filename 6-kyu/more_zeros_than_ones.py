def more_zeros(s):
    result = []
    seen = set()
    for ch in s:
        if ch in seen:
            continue
            
        seen.add(ch)
        bits = bin(ord(ch))[2:]
        zeros = bits.count('0')
        ones = bits.count('1')
        if zeros > ones:
            result.append(ch)

    return result