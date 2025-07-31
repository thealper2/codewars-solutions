def difference_of_squares(n):
    sum_of_square = (n * (n + 1) * (2 * n + 1)) / 6
    square_of_sum = ((n * (n + 1)) / 2) ** 2
    return square_of_sum - sum_of_square
