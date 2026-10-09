def valid_word(seq, word):
    n = len(word)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for w in seq:
            if i >= len(w) and word[i - len(w):i] == w and dp[i - len(w)]:
                dp[i] = True
                break

    return dp[n]