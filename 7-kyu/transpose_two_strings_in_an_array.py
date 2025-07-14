def transpose_two_strings(arr):
    if len(arr) != 2:
        return ""
    
    n1 = len(arr[0])
    n2 = len(arr[1])
    
    if n1 < n2:
        arr[0] += " " * (n2 - n1)
        n = n2
    elif n2 < n1:
        arr[1] += " " * (n1 - n2)
        n = n1
    else:
        n = n1
        
    result = []
    for i in range(n):
        result.append(f"{arr[0][i]} {arr[1][i]}")
    
    return "\n".join(result)