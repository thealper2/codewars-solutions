def split_odd_and_even(n):
    s = str(n)
    result = []
    current = s[0]
    for ch in s[1:]:
        if (int(ch) % 2) == (int(current[-1]) % 2):
            current += ch
        else:
            result.append(int(current))
            current = ch

    result.append(int(current))
    return result