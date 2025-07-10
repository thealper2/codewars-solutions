def phone_call(min1, min2_10, min11, s):
    total_minutes = 0
    if s >= min1:
        s -= min1
        total_minutes += 1
    else:
        return 0

    cost_for_9_minutes = 9 * min2_10
    if s >= cost_for_9_minutes:
        s -= cost_for_9_minutes
        total_minutes += 9
    else:
        total_minutes += s // min2_10
        return total_minutes

    total_minutes += s // min11
    return total_minutes
