def travel(total_time, run_time, rest_time, speed):
    total = 0
    while total_time > 0:
        run_duration = min(run_time, total_time)
        total += run_duration * speed
        total_time -= run_duration + rest_time
    return total