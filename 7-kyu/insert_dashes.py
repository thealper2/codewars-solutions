def insert_dash(num):
    num_str = str(num)
    result = [num_str[0]]

    for i in range(1, len(num_str)):
        prev_digit = int(num_str[i - 1])
        curr_digit = int(num_str[i])

        if prev_digit % 2 == 1 and curr_digit % 2 == 1:
            result.append('-')

        result.append(num_str[i])

    return ''.join(result)
