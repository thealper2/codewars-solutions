from datetime import timedelta


def period_is_late(last, today, cycle_length):
    return last + timedelta(days=cycle_length) < today
