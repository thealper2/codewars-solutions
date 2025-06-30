def trailing_zeros(n) -> int:
    i = n
    result = []
    while i >= 1:
        a = i % 2
        i = i // 2
        result[0:0] = str(a)

    result = result[::-1]
    count = 0
    for item in result:
        if int(item) == 1:
            break

        count += 1

    return count
