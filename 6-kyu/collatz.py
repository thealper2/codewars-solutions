def collatz(n):
    result = [n]
    while n != 1:
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n = n // 2
            
        result.append(n)
            
    return '->'.join(list(map(str, result)))