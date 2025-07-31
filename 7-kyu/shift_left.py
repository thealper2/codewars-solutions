def shift_left(a, b):
    len1 = len(a)
    len2 = len(b)
    min_len = min(len1, len2)
    common_suffix_length = 0

    for i in range(1, min_len + 1):
        if a[len1 - i] == b[len2 - i]:
            common_suffix_length += 1
        else:
            break

    return (len1 - common_suffix_length) + (len2 - common_suffix_length)
