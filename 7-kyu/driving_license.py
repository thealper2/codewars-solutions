import re


def driver(data):
    forename = data[0]
    middle_name = data[1] if len(data) > 1 and data[1] else None
    surname = data[2]
    dob_str = data[3]
    gender = data[4]

    surname_part = (surname.upper() + "99999")[:5]

    dob_parts = re.split("-| ", dob_str)
    day = int(dob_parts[0])
    month_str = dob_parts[1]
    year = int(dob_parts[2])

    decade_digit = (year // 10) % 10
    year_digit = year % 10

    month_map = {
        "Jan": 1,
        "Feb": 2,
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "Jun": 6,
        "Jul": 7,
        "Aug": 8,
        "Sep": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12,
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12,
    }
    month = month_map[month_str]
    if gender.upper() == "F":
        month += 50
    month_part = f"{month:02d}"

    day_part = f"{day:02d}"

    first_initial = forename[0].upper() if forename else "9"
    middle_initial = middle_name[0].upper() if middle_name else "9"
    initials_part = f"{first_initial}{middle_initial}"

    license_number = (
        f"{surname_part}"
        f"{decade_digit}"
        f"{month_part}"
        f"{day_part}"
        f"{year_digit}"
        f"{initials_part}"
        "9"
        "AA"
    )

    return license_number
