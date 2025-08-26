def swap_head_tail(arr):
    n = len(arr)
    if n <= 1:
        return arr
    
    if n % 2 == 0:
        mid = (n + 1) // 2
        return arr[-mid:] + arr[:mid]
    else:
        mid = (n - 1) // 2
        return arr[-mid:] + [arr[mid]] + arr[:mid]
