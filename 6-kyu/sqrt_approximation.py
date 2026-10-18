def sqrt_approximation(number):
    if number < 0:
        return None
    
    lo, hi = 0, number
    while lo <= hi:
        mid = (lo + hi) // 2
        sq = mid * mid
        if sq == number:
            return mid
        elif sq < number:
            lo = mid + 1
        else:
            hi = mid - 1
            
    return [hi, lo]