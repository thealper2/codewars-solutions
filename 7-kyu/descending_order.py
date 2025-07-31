def descending_order(num):
    nums = list(str(num))
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    return int("".join(nums))
