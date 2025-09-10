def determine_sequence(arr):
    n = len(arr)
    if n == 1:
        return 0
    
    is_ap = True
    is_gp = True
    d = arr[1] - arr[0]
    for i in range(2, n):
        if arr[i] - arr[i - 1] != d:
            is_ap = False
            break
            
    if arr[0] == 0:
        is_gp = False
    else:
        r = arr[1] / arr[0]
        for i in range(2, n):
            if arr[i - 1] == 0:
                is_gp = False
                break
                
            if arr[i] / arr[i - 1] != r:
                is_gp = False
                break
                
    if is_ap and is_gp:
        return 2
    elif is_ap:
        return 0
    elif is_gp:
        return 1
    else:
        return -1
