def missing_no(nums):
    expected_sum = 100 * 101 // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum
