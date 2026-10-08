def sum_dig_nth_term(init_val, pattern_l, nth_term):
    current_term = init_val
    n = len(pattern_l)
    for i in range(nth_term - 1):
        pattern = pattern_l[i % n]
        current_term = current_term + pattern

    return sum(int(d) for d in str(current_term))