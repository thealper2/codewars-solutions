def pyramid_height(n):
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid * (mid + 1) * (2 * mid + 1) // 6 <= n:
            lo = mid
        else:
            hi = mid - 1
            
    return lo