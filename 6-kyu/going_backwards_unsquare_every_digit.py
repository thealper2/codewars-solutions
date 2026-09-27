def unsquare_digits(result):
    chunks = {
        '0': '0', '1': '1', '4': '2', '9': '3', '16': '4',
        '25': '5', '36': '6', '49': '7', '64': '8', '81': '9',
    }
    s = str(result)
    n = len(s)

    dp = [[] for _ in range(n + 1)]
    dp[0] = ['']

    for i in range(1, n + 1):
        for length in (1, 2):
            j = i - length
            if j < 0 or not dp[j]:
                continue
            chunk = s[j:i]
            if chunk not in chunks:
                continue
            digit = chunks[chunk]
            for prefix in dp[j]:
                if prefix == '' and digit == '0' and n > 1:
                    continue
                dp[i].append(prefix + digit)

    if not dp[n]:
        return None
    
    return min(int(x) for x in dp[n])
