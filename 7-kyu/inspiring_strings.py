def longest_word(string_of_words):
    words = string_of_words.split()
    n = len(words)
    longest_word = ""

    for word in words:
        if len(longest_word) <= len(word):
            longest_word = word

    return longest_word
