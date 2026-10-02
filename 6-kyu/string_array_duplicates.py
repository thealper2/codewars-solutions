def dup(arry):
    result = []
    for word in arry:
        new_word = ''
        for c in word:
            if new_word and new_word[-1] == c:
                continue

            new_word += c

        result.append(new_word)

    return result