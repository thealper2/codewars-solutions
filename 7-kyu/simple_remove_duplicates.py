def solve(arr): 
    result = []
    seen = set()
    for num in arr[::-1]:
        if num not in seen:
            result.append(num)
        
        seen.add(num)
        
    return result[::-1]