def count_char_occurrences(strng, char):
    count = 0

    for c in strng:
        if c == char:
            count += 1

    return count
