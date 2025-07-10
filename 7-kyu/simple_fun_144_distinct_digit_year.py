def distinct_digit_year(year):
    year += 1
    while True:
        s = str(year)
        if len(s) == len(set(s)):
            return year
        year += 1
