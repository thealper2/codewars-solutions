def get_hours(shifts):
    def time_to_hours(time_str):
        time_str = time_str.lower()
        is_pm = 'pm' in time_str
        time_str = time_str.replace('am', '').replace('pm', '')
        hours, minutes = map(int, time_str.split(':'))
        if is_pm and hours != 12:
            hours += 12
        elif not is_pm and hours == 12:
            hours = 0
            
        return hours + minutes / 60
    
    result = []
    for shift in shifts:
        start, end = shift
        start_hours = time_to_hours(start)
        end_hours = time_to_hours(end)
        if end_hours < start_hours:
            end_hours += 24
            
        hours_worked = end_hours - start_hours
        hours_worked = round(hours_worked * 4) / 4.0
        result.append(hours_worked)
        
    return result
