def cube_times(times):
    max_ = max(times)
    times.remove(max_)
    min_ = min(times)
    times.remove(min_)
    avg = sum(times) / 3
    return (round(avg, 2), min_)
