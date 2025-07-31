def even_or_odd(s):
    sum_even = 0
    sum_odd = 0

    for c in s:
        if int(c) % 2 == 0:
            sum_even += int(c)
        else:
            sum_odd += int(c)

    if sum_odd > sum_even:
        return "Odd is greater than Even"

    elif sum_even > sum_odd:
        return "Even is greater than Odd"

    else:
        return "Even and Odd are the same"
