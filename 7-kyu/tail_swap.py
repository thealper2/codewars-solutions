def tail_swap(strings):
    first_parts = strings[0].split(':')
    second_parts = strings[1].split(':')
    new_first = first_parts[0] + ':' + second_parts[1]
    new_second = second_parts[0] + ':' + first_parts[1]
    return [new_first, new_second]
