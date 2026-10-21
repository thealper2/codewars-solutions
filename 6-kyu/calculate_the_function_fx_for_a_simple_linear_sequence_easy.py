def get_function(sequence):
    diffs = [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]
    if len(set(diffs)) != 1:
        return "Non-linear sequence"
    
    n = diffs[0]
    m = sequence[0]
    
    if n == 0:
        if m == 0:
            return "f(x) = 0"
        return f"f(x) = {m}"
    
    if n == 1:
        expr = "x"
    elif n == -1:
        expr = "-x"
    else:
        expr = f"{n}x"
    
    if m > 0:
        expr += f" + {m}"a
    elif m < 0:
        expr += f" - {abs(m)}"
    
    return f"f(x) = {expr}"