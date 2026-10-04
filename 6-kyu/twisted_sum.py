def compute_sum(n):
    return sum(sum(map(int, str(i))) for i in range(1, n + 1))