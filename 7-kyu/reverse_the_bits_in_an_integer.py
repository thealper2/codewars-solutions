def reverse_bits(n):
    bin_n = bin(n)[2:]
    return int(bin_n[::-1], 2)
