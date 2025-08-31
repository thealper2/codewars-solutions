def closest_pair_tonum(upper_limit):
    for m in range(upper_limit - 1, 0, -1):
        for n in range(m - 1, 0, -1):
            s = m + n
            d = m -n
            s_root = int(s**0.5)
            d_root = int(d**0.5)
            if s_root * s_root == s and d_root * d_root == d:
                return (m, n)
