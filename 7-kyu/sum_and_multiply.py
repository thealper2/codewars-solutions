def sum_and_multiply(sum, multiply):
    for left in range(sum):
        right = sum - left
        if left + right == sum and left * right == multiply:
            return [left, right]

    return None
