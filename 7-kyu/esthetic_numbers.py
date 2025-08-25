def esthetic(num):
    def number_to_base(n, base):
        digits = []
        while n:
            digits.append(int(n % base))
            n //= base
            
        return digits[::-1]
    
    result = []
    for i in range(2, 11):
        digits = number_to_base(num, i)
        n = len(digits)
        is_esthetic = True
        for j in range(n - 1):
            x, y = digits[j], digits[j + 1]
            if abs(x - y) != 1:
                is_esthetic = False
            
        if is_esthetic:
            result.append(i)
            
    return result
