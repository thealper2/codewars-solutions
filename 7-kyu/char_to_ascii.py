def char_to_ascii(s):
    if not s:
        return None

    result = {}
    seen = set()
    for c in s:
        if c not in seen and c.isalpha():
            seen.add(c)
            result[c] = ord(c)

    return result
