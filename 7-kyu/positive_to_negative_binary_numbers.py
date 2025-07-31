def positive_to_negative(binary):
    n = len(binary)
    if not binary:
        return []

    inverted = [1 - bit for bit in binary]
    carry = 1
    result = []
    for bit in reversed(inverted):
        sum_bit = bit + carry
        if sum_bit == 2:
            result.append(0)
            carry = 1
        else:
            result.append(sum_bit)
            carry = 0

    result.reverse()
    return result
