def calculate_age(year_of_birth, current_year):
    diff = current_year - year_of_birth
    if diff == 1:
        return "You are 1 year old."
    elif diff == -1:
        return "You will be born in 1 year."
    elif diff > 0:
        return f"You are {diff} years old."
    elif diff < 0:
        return f"You will be born in {-diff} years."
    else:
        return 'You were born this very year!'