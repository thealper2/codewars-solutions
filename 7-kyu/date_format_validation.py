import re

def date_checker(date):
    pattern = r'^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4} (0[0-9]|1[0-9]|2[0-3]):([0-5][0-9])$'
    return bool(re.fullmatch(pattern, date))