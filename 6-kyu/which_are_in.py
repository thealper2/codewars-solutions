def in_array(array1, array2):
    n1 = len(array1)
    n2 = len(array2)
    if n2 < n1:
        array1, array2 = array2, array1
        n1, n2 = n2, n1
        
    result = set()
    for i in range(n1):
        for j in range(n2):
            if array1[i] in array2[j]:
                result.add(array1[i])
                break
                
    return sorted(result)
