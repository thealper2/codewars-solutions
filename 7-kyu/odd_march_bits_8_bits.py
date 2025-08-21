def bit_march (n : int) -> list:
    result = []
    for i in range(8 - n + 1):
        a = 8 - n - i
        b = '0' * a + '1' * n + '0' * i
        result.append(list(map(int, list(b))))
        
    return result
