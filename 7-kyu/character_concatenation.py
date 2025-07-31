def char_concat(word):
    result = []
    n = len(word)
    for i in range(n // 2):
        left_char = word[i]
        right_char = word[n - 1 - i]
        result.append(f"{left_char}{right_char}{i + 1}")

    return "".join(result)
