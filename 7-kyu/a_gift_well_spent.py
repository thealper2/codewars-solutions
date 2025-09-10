def buy(c,arr):        
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == c:
                return [i, j]
            
    return None
