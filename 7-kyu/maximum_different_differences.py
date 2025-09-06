import math


def max_df(a_n: int) -> int:
    return (math.isqrt(a_n * 8) - 1) // 2
