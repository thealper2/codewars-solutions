def print_nums(*args):
    numbers = list(args)
    if not numbers:
        return ""

    if len(numbers) == 1:
        return str(numbers[0])

    max_num = max(numbers)
    max_length = len(str(max_num))
    formatted_numbers = []
    for num in numbers:
        num_str = str(num)
        if num == max_num:
            formatted_numbers.append(num_str)
        else:
            formatted_num = num_str.zfill(max_length)
            formatted_numbers.append(formatted_num)

    return "\n".join(formatted_numbers)
