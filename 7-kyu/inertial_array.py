def is_inertial(arr):
    if not arr:
        return False

    has_odd = any(x % 2 != 0 for x in arr)
    if not has_odd:
        return False

    max_val = max(arr)
    if max_val % 2 != 0:
        return False

    evens_not_max = [x for x in arr if x % 2 == 0 and x != max_val]
    odds = [x for x in arr if x % 2 != 0]

    if not evens_not_max:
        return True

    min_odd = min(odds)
    max_even_not_max = max(evens_not_max)

    return min_odd > max_even_not_max
