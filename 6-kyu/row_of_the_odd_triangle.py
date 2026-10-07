def odd_row(n):
    start_num = (n * n) - (n - 1)
    return [start_num + (2 * i) for i in range(n)]