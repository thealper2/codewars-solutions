def alphanumeric(password: str) -> bool:
    if password is None or not password:
        return False

    if '_' in password or ' ' in password:
        return False

    if not all(c.isalpha() or c.isdigit() for c in password):
        return False

    return True