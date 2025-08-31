def closing_in_sum(n):
    str_n = str(n)
    l, r = 0, len(str_n) - 1
    total = 0

    while l < r:
        num = f"{str_n[l]}{str_n[r]}"
        total += int(num)
        l += 1
        r -= 1
        
    if l == r:
        total += int(str_n[l])
        
    return total
