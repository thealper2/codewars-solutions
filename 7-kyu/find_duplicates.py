def duplicates(arr):
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            seen.add(num)
        else:
            if num not in result:
                result.append(num)
                
    return result
