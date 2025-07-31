def encode(st):
    result = ""
    for c in st:
        if 65 <= ord(c) <= 90:
            result += str(ord(c) % 64)
        elif 97 <= ord(c) <= 122:
            result += str(ord(c) % 96)
        else:
            result += c

    return result
