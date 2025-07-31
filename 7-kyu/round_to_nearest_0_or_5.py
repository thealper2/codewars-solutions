def round_to_five(arr):
    rounded_numbers = []
    for num in arr:
        quotient = num / 5
        rounded_quotient = int(quotient + 0.5) if quotient % 1 >= 0.5 else int(quotient)
        rounded_num = rounded_quotient * 5
        rounded_numbers.append(rounded_num)

    return rounded_numbers
