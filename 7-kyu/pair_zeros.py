def pair_zeros(arr):
    zero_count = 0
    result = []
    for num in arr:
        if num == 0:
            zero_count += 1
            if zero_count % 2 == 0:
                continue

        result.append(num)
    return result
