def max_ball(v0):
    v0_ms = v0 * 1000 / 3600
    g = 9.81
    t_peak = v0_ms / g
    k = round(t_peak * 10)

    def h(k):
        t = k / 10.0
        return v0_ms * t - 0.5 * g * t * t

    best = k
    for cand in (k - 1, k, k + 1):
        if cand >= 0 and h(cand) > h(best):
            best = cand

    return best