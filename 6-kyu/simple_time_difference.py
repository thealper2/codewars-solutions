def solve(alarms):
    minutes = sorted(set(int(t[:2]) * 60 + int(t[3:]) for t in alarms))
    n = len(minutes)
    if n == 1:
        return "23:59"

    best = 0
    for i in range(n):
        j = (i + 1) % n
        if j == 0:
            gap = (minutes[j] + 1440) - minutes[i]
        else:
            gap = minutes[j] - minutes[i]
        if gap > best:
            best = gap

    silent = best - 1
    return f"{silent // 60:02d}:{silent % 60:02d}"