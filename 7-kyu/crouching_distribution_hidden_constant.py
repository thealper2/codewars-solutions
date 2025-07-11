def find_constant(arr, lb, ub):
    expected_mean = (lb + ub) / 2
    actual_mean = sum(arr) / len(arr)
    constant = actual_mean - expected_mean
    return round(constant)
