def set_the_alarms_up(time, n):
    hours, minutes = map(int, time.split(':'))
    result = [time]
    for _ in range(n - 1):
        minutes += 5
        if minutes >= 60:
            hours += 1
            minutes -= 60
            
        if hours >= 24:
            hours = 0
            
        result.append(f'{hours:02d}:{minutes:02d}')
        
    return result
            
