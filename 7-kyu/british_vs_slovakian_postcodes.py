import re


def which_postcode(postcode):
    postcode = postcode.strip()
    gb_pattern = re.compile(r'^[A-Za-z]{1,2}\d{1,2} \d[A-Za-z]{2}$', re.IGNORECASE)
    sk_pattern = re.compile(r'^\d{3} \d{2}$')
    
    if gb_pattern.fullmatch(postcode):
        return "GB"
    elif sk_pattern.fullmatch(postcode):
        return "SK"
    else:
        return "Not valid"
