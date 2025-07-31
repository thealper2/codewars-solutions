def status(nums):
    elements_with_status = []
    for index, num in enumerate(nums):
        less_count = sum(1 for x in nums if x < num)
        status = index + less_count
        elements_with_status.append((status, index, num))

    elements_with_status.sort(key=lambda x: (x[0], x[1]))
    result = [num for status, index, num in elements_with_status]
    return result
