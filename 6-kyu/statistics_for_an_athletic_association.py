def stat(strg):
    if not strg:
        return ''

    def to_seconds(t):
        h, m, s = t.split('|')
        return int(h) * 3600 + int(m) * 60 + int(s)

    def to_time(sec):
        sec = int(sec)
        h, rem = divmod(sec, 3600)
        m, s = divmod(rem, 60)
        return f'{h:02d}|{m:02d}|{s:02d}'

    times = sorted(to_seconds(part.strip()) for part in strg.split(','))

    rng = times[-1] - times[0]
    avg = sum(times) // len(times)

    n = len(times)
    if n % 2 == 1:
        median = times[n // 2]
    else:
        median = (times[n // 2 - 1] + times[n // 2]) // 2

    return f'Range: {to_time(rng)} Average: {to_time(avg)} Median: {to_time(median)}'