def arrange(s):
    words = s.split()
    for i in range(len(words) - 1):
        if i % 2 == 0:
            if len(words[i]) > len(words[i + 1]):
                words[i], words[i + 1] = words[i + 1], words[i]
        else:
            if len(words[i]) < len(words[i + 1]):
                words[i], words[i + 1] = words[i + 1], words[i]

    return ' '.join(
        w.lower() if i % 2 == 0 else w.upper()
        for i, w in enumerate(words)
    )