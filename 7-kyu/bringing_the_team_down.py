def lowest_possible_place(n, score):
    sum_top_n = n * (n + 1) // 2
    max_k = score - sum_top_n - 1
    if max_k >= n + 1:
        return max_k
    else:
        return -1