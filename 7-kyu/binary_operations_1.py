def flip_bit(value, index):
    binary = bin(value)[2:]
    if index > len(binary):
        binary = binary.zfill(index)

    index_from_left = len(binary) - index
    if index_from_left >= 0:
        flipped = list(binary)
        flipped[index_from_left] = "1" if flipped[index_from_left] == "0" else "0"
        flipped = "".join(flipped)
    else:
        flipped = "1" + "0" * (abs(index_from_left) - 1) + binary

    return int(flipped, 2)
