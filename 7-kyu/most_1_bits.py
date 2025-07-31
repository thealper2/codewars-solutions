def most_one_bits(nums: list[int]) -> int:
    seen = set()
    max_count = -1
    result = None
    for num in nums:
        if num in seen:
            continue
        seen.add(num)
        if num < 0:
            binary = bin(num & 0xFF)[2:].zfill(8)
        else:
            binary = bin(num)[2:].zfill(8)[-8:]
        count = binary.count("1")
        if count >= max_count:
            max_count = count
            result = numa
    return result
