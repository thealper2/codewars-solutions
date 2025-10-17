def biggest(nums):
    if not nums:
        return '0'
        
    nums_str = list(map(str, nums))
    n = len(nums_str)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums_str[j] + nums_str[j + 1] < nums_str[j + 1] + nums_str[j]:
                nums_str[j], nums_str[j + 1] = nums_str[j + 1], nums_str[j]
                
    result = ''.join(nums_str)
    return result if result[0] != '0' else '0'
