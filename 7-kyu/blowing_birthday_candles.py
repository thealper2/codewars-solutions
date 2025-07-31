def blow_candles(s):
    moves = 0
    s = list(s)
    n = len(s)
    while True:
        if all(c == "0" for c in s):
            break

        left = 0
        while left < n and s[left] == "0":
            left += 1

        length = min(3, n - left)
        for i in range(left, left + length):
            if s[i] != "0":
                s[i] = str(int(s[i]) - 1)

        moves += 1

    return moves
