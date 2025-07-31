def solve(arr):
    s = set()
    num = 0

    for item in arr:
        if item not in s:
            s.add(item)
            num += item

    return num
