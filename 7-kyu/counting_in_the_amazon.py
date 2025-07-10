def count_arara(n):
    base = " ".join(["adak"] * (n // 2))
    
    if n == 1:
        return "anane"
    
    if n % 2 != 0:
        return f"{base} anane" if base else "anane"
    
    return base
