def approx_root(n):
    base = int(n ** 0.5)
    if base * base == n:
        return base
    
    lower_sq = base * base
    higher_sq = (base + 1) ** 2
    diff_gn = n - lower_sq
    diff_lg = higher_sq - lower_sq
    result = base + (diff_gn / diff_lg)
    return round(result, 2)
