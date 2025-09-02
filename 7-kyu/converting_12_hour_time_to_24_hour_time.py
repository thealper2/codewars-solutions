def to24hourtime(hour, minute, period):
    if hour == 12 and period == 'am':
        hour = 0
    elif hour < 12 and period == 'pm':
        hour += 12

    return f'{hour:02d}{minute:02d}'
