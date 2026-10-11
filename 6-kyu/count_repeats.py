def count_repeats(txt):
    return sum(1 for i in range(1, len(txt)) if txt[i] == txt[i - 1])