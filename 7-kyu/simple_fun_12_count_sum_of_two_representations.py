def count_sum_of_two_representations(n, l, r):
    count = 0
    for A in range(l, r + 1):
        B = n - A
        if l <= B <= r and A <= B:
            count += 1

    return count
