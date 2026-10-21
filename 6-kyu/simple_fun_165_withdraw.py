def withdraw(n):
    for hundreds in range(n // 100, -1, -1):
        remainder = n - hundreds * 100
        for fifties in range(remainder // 50, -1, -1):
            rest = remainder - fifties * 50
            if rest % 20 == 0:
                return [hundreds, fifties, rest // 20]
            
    return []