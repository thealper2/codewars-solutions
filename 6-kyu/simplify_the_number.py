def simplify(number): 
    s = str(number)
    length = len(s)
    parts = []
    
    for i, ch in enumerate(s):
        if ch != '0':
            power = length - i - 1
            if power == 0:
                parts.append(ch)
            else:
                parts.append(f"{ch}*{10 ** power}")
                
    return "+".join(parts)