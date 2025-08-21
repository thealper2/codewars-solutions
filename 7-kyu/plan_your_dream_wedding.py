def max_wedding_cost(C, r, S, T, W):
    r_decimal = r / 100.0
    n = T * 12
    m = W * 12
    k = (T - W) * 12
    A = C * ((1 + r_decimal)**n - 1) / r_decimal
    B = C * ((1 + r_decimal)**m - 1) / r_decimal
    if A < S:
        return 0.0
    
    X_retirement = (A - S) / ((1 + r_decimal)**k)
    X_max = min(B, X_retirement)
    return X_max
