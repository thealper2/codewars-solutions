def ball_test(s, r):
    position = 0
    n = len(r)
    while s > 0 and position < n:
        segment_end = min(position + s, n)
        segment = r[position:segment_end]
        crack_count = segment.count('x')
        position += s
        s = s - 1 - crack_count
        
    return position >= n