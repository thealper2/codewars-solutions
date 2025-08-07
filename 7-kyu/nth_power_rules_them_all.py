def modified_sum(a, n):
    x = sum(i ** n for i in a)
    y = sum(a)
    return x - y
