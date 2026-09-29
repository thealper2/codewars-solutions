def diamond(n):
    if n % 2 == 0 or n <= 0:
        return None
    
    result = []
    for i in range(1, n + 1, 2):
        result.append(" " * ((n - i) // 2) + "*" * i)
        
    for i in range(n - 2, 0, -2):
        result.append(" " * ((n - i) // 2) + "*" * i)
    
    return "\n".join(result) + "\n"