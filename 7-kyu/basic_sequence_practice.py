def sum_of_n(n):
    length = abs(n) + 1
    series = [0]
    for i in range(1, length):
        if n > 0:
            series.append(series[-1] + i)
        else:
            series.append(series[-1] - i)
            
    return series