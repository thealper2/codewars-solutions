def geo_mean(nums, arith_mean):
    missing = (arith_mean * (len(nums) + 1)) - sum(nums)
    nums.append(missing)
    product = 1
    for num in nums:
        product *= num
        
    return product ** (1 / len(nums))