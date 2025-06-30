def was_package_received_yesterday(tz_from, tz_to, start, duration):
    return start < tz_from - tz_to - duration