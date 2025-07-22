import re
from datetime import datetime, timedelta

def date_correct(date):
    if not date:
        return date
    
    pattern = r"(\d{2}\.){2}\d{4}"
    
    if re.fullmatch(pattern, date):
        day, month, year = map(int, date.split("."))
        plus_years, month = divmod(month, 12)
        year += plus_years
        
        if month == 0:
            month = 12
            year -= 1
        
        new_date = datetime(year, month, 1) + timedelta(days=day - 1)
        corrected_date_str = f"{new_date.day:02d}.{new_date.month:02d}.{new_date.year}"
        return corrected_date_str