def four_seasons(day):
    if day > 365:
        return "The year flew by!"
    if 1 <= day <= 79 or 355 <= day <= 365:
        return "Winter Season"
    elif 80 <= day <= 171:
        return "Spring Season"
    elif 172 <= day <= 263:
        return "Summer Season"
    else:
        return "Autumn Season"
