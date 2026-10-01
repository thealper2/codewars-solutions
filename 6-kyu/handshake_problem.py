from math import isqrt

def get_participants(handshakes):
    if handshakes <= 0:
        return 0

    n = (1 + isqrt(1 + 8 * handshakes)) // 2
    while n * (n - 1) // 2 < handshakes:
        n += 1

    return n