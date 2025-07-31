def common_ground(s1, s2):
    words_s1 = s1.split()
    words_s2 = s2.split()

    set_s1 = set(words_s1)
    common_words = []
    seen_words = set()

    for word in words_s2:
        if word in set_s1 and word not in seen_words:
            common_words.append(word)
            seen_words.add(word)

    if not common_words:
        return "death"
    else:
        return " ".join(common_words)
