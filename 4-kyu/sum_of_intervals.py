def sum_of_intervals(intervals):
    if not intervals:
        return 0
    
    sorted_intervals = sorted(intervals)
    total = 0
    cur_start, cur_end = sorted_intervals[0]
    for start, end in sorted_intervals[1:]:
        if start <= cur_end:
            cur_end = max(cur_end, end)
        else:
            total += cur_end - cur_start
            cur_start, cur_end = start, end
            
    total += cur_end - cur_start
    return total