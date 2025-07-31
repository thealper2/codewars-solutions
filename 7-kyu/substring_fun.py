def nth_char(words):
    if not words:
        return ""

    n = len(words)
    result = ""
    for i in range(n):
        result += words[i][i]

    return result
