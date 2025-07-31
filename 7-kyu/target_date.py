import math
from datetime import datetime, timedelta


def date_nb_days(a0, a, p):
    daily_rate = p / 36000
    days = math.log(a / a0) / math.log(1 + daily_rate)
    days = math.ceil(days)

    start_date = datetime(2016, 1, 1)
    end_date = start_date + timedelta(days=days)

    return end_date.strftime("%Y-%m-%d")
