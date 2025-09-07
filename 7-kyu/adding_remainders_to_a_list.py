def solve(nums, div):
    return [num + (num % div) for num in nums]
