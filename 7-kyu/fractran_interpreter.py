def fractran(code: str, n: int) -> int:
    fractions = [tuple(map(int, frac.split('/'))) for frac in code.split()]
    for _ in range(1000):
        found = False
        for num, den in fractions:
            if n * num % den == 0:
                n = n * num // den
                found = True
                break
        
        if not found:
            break
            
    return n
