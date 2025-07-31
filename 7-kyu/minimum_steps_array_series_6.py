def minimum_steps(numbers, value):
    numbers.sort()
    sum_ = 0
    operations = -1
    for num in numbers:
        sum_ += num
        operations += 1
        if sum_ >= value:
            return operations

    return -1
