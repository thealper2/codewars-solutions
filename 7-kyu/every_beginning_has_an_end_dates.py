from datetime import datetime, timedelta


def week_start_date(dt):
    return dt - timedelta(days=dt.weekday())


def week_end_date(dt):
    return dt + timedelta(days=6 - dt.weekday())
