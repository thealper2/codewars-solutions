def vowel_indices(word):
    n = len(word)
    vowels = {"a", "e", "i", "o", "u", "y"}
    result = []

    for i in range(n):
        if word[i].lower() in vowels:
            result.append(i + 1)

    return result
