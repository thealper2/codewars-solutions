def get_best_word(points, words):
    best_idx = 0
    best_score = -1
    best_len = float('inf')
    for i, word in enumerate(words):
        score = sum(points[ord(ch) - ord('A')] for ch in word)
        length = len(word)
        if score > best_score or (score == best_score and length < best_len):
            best_score = score
            best_len = length
            best_idx = i

    return best_idx