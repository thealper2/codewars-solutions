def tunnel_digging(r):
    stop_time = len(r) // 3 * 30
    section_times = {
        '[': 30, ']': 30,
        '{': 25, '}': 25,
        '(': 20, ')': 20,
        '|': 15, ':': 10
    }
    
    r = ''.join(r)
    for section in r:
        time = section_times.get(section, 0)
        stop_time += time
    
    return stop_time
