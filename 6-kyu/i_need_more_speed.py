def reverse(seq):
    i, j = 0, len(seq) - 1

    while i < j:
        seq[i], seq[j] = seq[j], seq[i]
        i += 1
        j -= 1