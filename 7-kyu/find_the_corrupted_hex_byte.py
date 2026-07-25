HEX = set("0123456789ABCDEF")

def find_corrupted_byte(dump):
    for i, b in enumerate(dump):
        if len(b) != 2:
            return i
        
        if b[0] not in HEX or b[1] not in HEX:
            return i
        
    return -1
