def pisano(n):
    prev, curr = 0, 1
    for i in range(1, n * n + 1):
        prev, curr = curr, (prev + curr) % n
        if prev == 0 and curr == 1:
            return i
