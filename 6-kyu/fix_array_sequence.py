def solve(arr):
    nums = set(arr)
    for num in arr:
        if (num * 3 not in nums) and (num % 2 != 0 or num // 2 not in nums):
            start = num
            break
            
    result = [start]
    current = start
    
    while len(result) < len(arr):
        if current % 3 == 0 and current // 3 in nums:
            current = current // 3
            result.append(current)
        elif current * 2 in nums:
            current = current * 2
            result.append(current)
            
    return result
