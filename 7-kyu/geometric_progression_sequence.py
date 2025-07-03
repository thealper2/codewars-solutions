def geometric_sequence_elements(a, r, n):
    result = [a]
    for i in range(n - 1):
        result.append(result[-1] * r)
        
    return ', '.join(str(item) for item in result)