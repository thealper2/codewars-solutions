def is_magic_three(arr: list[int]) -> bool:
    s = set(arr)
    nums = list(s)
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            target = -(arr[i] + arr[j])
            if target in s:
                return True
    return False