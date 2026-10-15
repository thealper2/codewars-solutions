def regression_line(x, y):
    """ Return the a (intercept)
        and b (slope) of Regression Line
        (Y on X).
    """
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_x2 = sum(xi * xi for xi in x)

    denom = n * sum_x2 - sum_x * sum_x
    a = (sum_x2 * sum_y - sum_x * sum_xy) / denom
    b = (n * sum_xy - sum_x * sum_y) / denom

    return (round(a, 4), round(b, 4))