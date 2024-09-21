def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return sum(arr[1:len(arr)-1])