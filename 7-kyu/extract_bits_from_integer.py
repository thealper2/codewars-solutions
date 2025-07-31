def extract_bits(field: int, offset: int, length: int):
    if length == 0:
        return 0
    masked_input = field & 0xFFFFFFFFFFFFFFFF
    if offset >= 64:
        return 0
    effective_length = min(length, 64 - offset)
    if effective_length <= 0:
        return 0
    shifted = masked_input >> offset
    mask = (1 << effective_length) - 1
    result = shifted & mask
    return result
