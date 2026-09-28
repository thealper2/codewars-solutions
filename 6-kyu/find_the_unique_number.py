def find_uniq(arr):
    a, b, c = arr[0], arr[1], arr[2]
    if a == b or a == c:
        common = a
    else:
        common = b
        
    for x in arr:
        if x != common:
            return x