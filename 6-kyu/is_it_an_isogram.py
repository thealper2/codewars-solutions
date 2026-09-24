def is_isogram(word: str) -> bool:
    if not word:
        return False

    chars = {}
    for c in word.lower():
        if c.isalpha():
            chars[c] = chars.get(c, 0) + 1

    if not chars:
        return False

    return sum(chars.values()) / len(chars) == list(chars.values())[0]