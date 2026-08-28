def vertical(words):
    if not words:
        return ""

    max_len = max(len(w) for w in words)
    result = []

    for i in range(max_len):
        row_chars = []
        for word in words:
            if i < len(word):
                row_chars.append(word[i])
            else:
                row_chars.append(" ")

        result.append(" ".join(row_chars).rstrip())

    return "\n".join(result)