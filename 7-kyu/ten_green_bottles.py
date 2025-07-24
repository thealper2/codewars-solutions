def ten_green_bottles(n):
    result = []
    bottles = ['no', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    for i in range(n, 0, -1):
        current = bottles[i]
        next_bottle = bottles[i - 1]
        line1 = f"{current.capitalize()} green {'bottle' if i == 1 else 'bottles'} hanging on the wall,"
        result.append(line1)
        result.append(line1)

        if i == 1:
            third_line = "If that one green bottle should accidentally fall,"
        else:
            third_line = "And if one green bottle should accidentally fall,"
        
        result.append(third_line)
        fourth_line = f"There'll be {next_bottle} green {'bottle' if i - 1 == 1 else 'bottles'} hanging on the wall."
        result.append(fourth_line)
        if i > 1:
            result.append('')

    return '\n'.join(result) + "\n"
