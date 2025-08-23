def hex_hash(code):
    result = 0
    for c in code:
        hex_c = hex(ord(c))[2:]
        for d in hex_c:
            if d.isdigit():
                result += int(d)
                
    return result
