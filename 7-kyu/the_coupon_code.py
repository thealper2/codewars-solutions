from datetime import datetime

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if type(entered_code) != type(correct_code) or entered_code != correct_code:
        return False
    
    current = datetime.strptime(current_date, "%B %d, %Y")
    expiration = datetime.strptime(expiration_date, "%B %d, %Y")
    return current <= expiration
