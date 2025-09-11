def validate(username, password):
    m, n = len(username), len(password)
    shortest = min(m, n)
    half = shortest / 2

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    longest = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if username[i - 1] == password[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                longest = max(longest, dp[i][j])

    return longest < half
