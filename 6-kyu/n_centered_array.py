def is_centered(arr: list[int], N: int) -> bool:
    if not arr:
        return N == 0
    
    total = len(arr)
    prefix = [0]
    for v in arr:
        prefix.append(prefix[-1] + v)
        
    for trim in range(total // 2 + 1):
        l, r = trim, total - trim
        if l > r:
            break
            
        sub_sum = prefix[r] - prefix[l]
        if sub_sum == N:
            return True
        
    return False
