def find_all(array, n):
    l = len(array)
    result = []
    
    for i in range(l):
        if array[i] == n:
            result.append(i)
            
    return result