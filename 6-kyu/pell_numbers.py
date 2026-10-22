def pell(n):
    numbers = [0, 1]

    for i in range(2, n + 1):
        numbers.append(2 * numbers[i - 1] + numbers[i - 2])

    return numbers[n]