def square_or_square_root(arr):
    return [item ** 2 if (item ** 0.5) != int(item ** 0.5) else item ** 0.5 for item in arr]