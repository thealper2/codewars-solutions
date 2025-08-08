def determine_time(arr):
    total_seconds = 0
    for duration in arr:
        hh, mm, ss = map(int, duration.split(':'))
        total_seconds += hh * 3600 + mm * 60 + ss
        
    return total_seconds <= 86400
