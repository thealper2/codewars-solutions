import re


def validate_number(st):
    if not st:
        return "Plenty more fish in the sea"
    
    cleaned = re.sub(r'-', '', st)
    pattern = r'^(07\d{9}|447\d{9}|\+447\d{9})$'
    if re.fullmatch(pattern, cleaned):
        return "In with a chance"
    else:
        return "Plenty more fish in the sea"
