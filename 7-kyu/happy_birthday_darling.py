def womens_age(n):
    def number_to_base(num, b):
        if num == 0:
            return [0]
        digits = 0
        i = 0
        while num:
            digits += int(num % b) * (10 ** i)
            num //= b
            i += 1
            
        return digits
    
    for i in range(2, n):
        a = number_to_base(n, i)
        if a == 20:
            return f"{n}? That's just 20, in base {i}!"
        elif a == 21:
            return f"{n}? That's just 21, in base {i}!"
        
    return -1
