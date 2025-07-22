def clock_degree(s) :
    hours, minutes = map(int, s.split(':'))
    if not (0 <= hours < 24 and 0 <= minutes < 60):
        return 'Check your time !'

    hour_deg = (hours % 12) * 30
    if hour_deg == 0:
        hour_deg = 360

    minute_deg = minutes * 6
    if minute_deg == 0:
        minute_deg = 360

    return f"{hour_deg}:{minute_deg}"