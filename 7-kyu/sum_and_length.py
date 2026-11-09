def sum_length(arr: list[int]) -> str:
    p1, p2 = 0, 0
    sum_zero = True
    for item in arr:
        if item <= 0:
            if item == 0:
                if sum_zero:
                    p2 += 1
                sum_zero = not sum_zero
            else:
                p2 += 1
        else:
            p1 += item
    return f"{p1} {p2}"