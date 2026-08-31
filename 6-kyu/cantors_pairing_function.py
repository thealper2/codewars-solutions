def cantor(n : int) -> str:
    d = 1
    while d * (d + 1) // 2 < n:
        d += 1
    
    pos_in_diag = n - (d - 1) * d // 2
    
    if d % 2 == 1:
        numerator = d - pos_in_diag + 1
        denominator = pos_in_diag
    else:
        numerator = pos_in_diag
        denominator = d - pos_in_diag + 1
    
    return f"{numerator}/{denominator}"