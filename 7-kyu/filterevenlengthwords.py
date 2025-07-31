def filter_even_length_words(words):
    result = []
    for word in words:
        if len(word) % 2 == 0:
            result.append(word)

    return result
