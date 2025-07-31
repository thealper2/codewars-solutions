def check_logs(log):
    if not log:
        return 0

    n = len(log)
    count = 1
    for i in range(1, n):
        prev_time = log[i - 1].split(":")
        current_time = log[i].split(":")

        prev_h, prev_m, prev_s = map(int, prev_time)
        curr_h, curr_m, curr_s = map(int, current_time)

        if curr_h < prev_h:
            count += 1
        elif curr_h == prev_h:
            if curr_m < prev_m:
                count += 1
            elif curr_m == prev_m and curr_s <= prev_s:
                count += 1

    return count
