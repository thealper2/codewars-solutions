def eq_sum_powdig(h_max, exp):
    result = []
    for num in range(2, h_max + 1):
        squared = 0
        for d in str(num):
            squared += int(d) ** exp

        if squared == num:
            result.append(num)

    return result
