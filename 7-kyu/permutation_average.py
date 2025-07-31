from itertools import permutations


def permutation_average(n):
    digits = list(str(n))
    unique_perms = set(permutations(digits))
    total = 0
    count = 0
    for perm in unique_perms:
        num = int("".join(perm))
        total += num
        count += 1

    average = total / count
    return round(average)
