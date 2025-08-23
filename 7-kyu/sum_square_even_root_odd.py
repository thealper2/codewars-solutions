def sum_square_even_root_odd(nums):
    n = len(nums)
    for i in range(n):
        if nums[i] % 2 == 0:
            nums[i] = nums[i] ** 2
        else:
            nums[i] = nums[i] ** 0.5
            
    result = sum(nums)
    return round(result, 2)
