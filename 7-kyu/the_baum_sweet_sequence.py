def baum_sweet():
    n = 0
    yield 1
    while True:
        n += 1
        binary = bin(n)[2:]
        has_odd_zero_block = False
        zero_block_length = 0

        for bit in binary:
            if bit == "0":
                zero_block_length += 1
            else:
                if zero_block_length > 0 and zero_block_length % 2 != 0:
                    has_odd_zero_block = True
                    break

                zero_block_length = 0

        if zero_block_length > 0 and zero_block_length % 2 != 0:
            has_odd_zero_block = True

        yield 0 if has_odd_zero_block else 1
