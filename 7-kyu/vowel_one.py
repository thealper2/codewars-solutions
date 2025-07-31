def vowel_one(s):
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    result = []
    for char in s:
        if char in vowels:
            result.append("1")
        else:
            result.append("0")
    return "".join(result)
