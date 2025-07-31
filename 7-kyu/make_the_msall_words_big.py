def small_word_helper(sentence):
    words = sentence.split()
    result = []
    vowels = {"a", "e", "i", "o", "u"}
    for word in words:
        n = len(word)
        if n <= 3:
            result.append(word.upper())
        else:
            temp = ""
            for c in word:
                if c.lower() not in vowels:
                    temp += c

            result.append(temp)

    return " ".join(result)
