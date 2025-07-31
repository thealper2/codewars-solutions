def make_sequences(n):
    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = 1
        for k in range(1, i // 2 + 1):
            dp[i] += dp[k]

    return dp[n]
