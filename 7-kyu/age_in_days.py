from datetime import datetime, date

def age_in_days(year, month, day):
    now = datetime.now().date()
    d = date(year, month, day)
    delta = now - d
    return f'You are {delta.days} days old'
