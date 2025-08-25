def word_pattern(word):
    word = word.lower()
    pattern = []
    mapping = {}
    count = 0
    for char in word:
        if char not in mapping:
            mapping[char] = count
            count += 1
        pattern.append(str(mapping[char]))

    return '.'.join(pattern)
