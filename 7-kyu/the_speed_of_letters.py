def speedify(st):
    if not st:
        return ""

    max_shift = 25
    max_length = len(st) + max_shift
    output = [" "] * max_length

    for idx, char in enumerate(st):
        shift = ord(char) - ord("A")
        new_pos = idx + shift
        if new_pos < max_length:
            output[new_pos] = char

    result = "".join(output).rstrip()
    return result
