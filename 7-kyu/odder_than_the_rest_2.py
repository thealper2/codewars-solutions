def oddest(a):
    def to_reversed_binary(x):
        if x < 0:
            x = (1 << 32) + x
        binary = bin(x)[2:]
        return binary[::-1]

    reversed_binaries = [to_reversed_binary(x) for x in a]
    max_index = 0
    for i in range(1, len(reversed_binaries)):
        if reversed_binaries[i] > reversed_binaries[max_index]:
            max_index = i

    return a[max_index]
