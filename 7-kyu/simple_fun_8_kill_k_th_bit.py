def kill_kth_bit(n, k):
    mask = 1 << (k - 1)
    if n & mask:
        return n & ~mask
    else:
        return n
