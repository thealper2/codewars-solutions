import re

def validate_code(code):
    return re.match(r"^[1-3]", str(code)) is not None
