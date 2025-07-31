def solve(st):
    n = min(len(st) // 2, len(st) - 1)
    max_len = 0

    for l in range(n, 0, -1):
        if st[:l] == st[-l:]:
            max_len = l
            break

    return max_len
