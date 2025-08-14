def permutation_shift(lst):
    shifts = [num - idx for idx, num in enumerate(lst)]
    max_shift = max(shifts)
    min_shift = min(shifts)
    return max_shift - min_shift
