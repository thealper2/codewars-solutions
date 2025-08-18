def divisible_by_last(n):
    digits = list(map(int, str(n)))
    result = [False]

    for i in range(1, len(digits)):
        prev, curr = digits[i - 1], digits[i]
        if prev == 0:
            result.append(False)
        else:
            result.append(curr % prev == 0)
            
    return result
