def convert_to_minute(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

def check_availability(schedule, current_time):
    current_minute = convert_to_minute(current_time)
    for meeting in schedule:
        start = convert_to_minute(meeting[0])
        end = convert_to_minute(meeting[1])
        
        if start <= current_minute < end:
            return meeting[1]
        
    return True
