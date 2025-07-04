import datetime


def gigasecond(start_date):
    gigasecond_to_day = (10 ** 9) / (60 * 60 * 24)
    end_date = start_date + datetime.timedelta(days=gigasecond_to_day)
    return end_date
