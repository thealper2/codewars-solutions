def create_phone_number(n):
    nums = list(map(str, n))
    p1 = ''.join(nums[0:3])
    p2 = ''.join(nums[3:6])
    p3 = ''.join(nums[6:])
    return f"({p1}) {p2}-{p3}"
