def rotate(xs: list, n: int) -> list:
    arr = xs.copy()
    if n == 0:
        return arr
    
    l = len(arr)
    n = n % l
    if n > 0:
        return arr[-n:] + arr[:l-n]
    else:
        return arr[-n:] + arr[:-n]