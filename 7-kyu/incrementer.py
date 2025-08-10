def incrementer(nums):
    result = []
    for i, num in enumerate(nums, start=1):
        result.append((num + i) % 10)
        
    return result