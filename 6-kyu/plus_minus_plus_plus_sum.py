def is_possible(arr, target):
    n = len(arr)
    sums = {arr[0]}
    for i in range(1, n):
        new_sums = set()
        for s in sums:
            new_sums.add(s + arr[i])
            new_sums.add(s - arr[i])
            
        sums = new_sums
        
    return target in sums
