from typing import defaultdict


def unscramble(scramble):
    global word_list
    scrambled_count = defaultdict(int)
    for letter in scramble.lower():
        scrambled_count[letter] += 1

    valid_words = []
    for word in word_list:
        word_count = defaultdict(int)
        for letter in word.lower():
            word_count[letter] += 1
        if word_count == scrambled_count:
            valid_words.append(word)

    return valid_words
