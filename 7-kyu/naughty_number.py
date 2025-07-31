def naughty_number(arr):
    for index, sub_array in enumerate(arr):
        stack = sub_array.copy()
        found = None
        while stack:
            current = stack.pop()
            if isinstance(current, list):
                stack.extend(current)
            else:
                found = current
                break

        if found is not None:
            return index

    return -1
