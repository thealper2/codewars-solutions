import re


def validate_usr(username):
    pattern = r"^[a-z0-9_]+$"
    if re.match(pattern, username) and 4 <= len(username) <= 16:
        return True
    else:
        return False
