import time

def increment_loop(n):
    if n == 0:
        return 0
    
    i = 0
    end_time = time.time() + n
    while time.time() < end_time:
        i += 1
    
    return i
