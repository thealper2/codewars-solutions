def run_length_encoding(s):
    if not s:
        return []

    result = []
    c = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            c += 1
        else:
            result.append([c, s[i - 1]])
            c = 1

    result.append([c, s[-1]])
    return result