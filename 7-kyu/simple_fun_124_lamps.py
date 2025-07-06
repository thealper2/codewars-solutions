def lamps(a):
    n = len(a)
    switches_pattern1 = 0
    for i in range(n):
        expected = 1 if i % 2 == 0 else 0
        if a[i] != expected:
            switches_pattern1 += 1
    
    switches_pattern0 = 0
    for i in range(n):
        expected = 0 if i % 2 == 0 else 1
        if a[i] != expected:
            switches_pattern0 += 1
    
    return min(switches_pattern1, switches_pattern0)