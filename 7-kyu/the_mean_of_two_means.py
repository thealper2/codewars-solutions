def get_mean(arr,x,y):
    n = len(arr)
    if x < 2 or y < 2 or x > n or y > n:
        return -1
    
    a = sum(arr[:x]) / x
    b = sum(arr[-y:]) / y
    return (a + b) / 2
