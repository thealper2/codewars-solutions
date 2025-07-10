def last(s):
    words = s.split()
    return sorted(words, key=lambda word: word[-1])
