def check_vowel(strng, position):
    if position > len(strng) - 1 or position < 0:
        return False

    return strng[position].lower() in {"a", "e", "i", "o", "u"}
