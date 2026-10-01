def xbonacci(signature, n):
    result = signature[:n]
    x = len(signature)
    window_sum = sum(result)
    while len(result) < n:
        result.append(window_sum)
        window_sum += result[-1] - result[-1 - x]

    return result