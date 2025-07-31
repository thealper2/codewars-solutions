def sort_it(words, n):
    return ", ".join(sorted(words.split(", "), key=lambda x: x[n - 1]))
