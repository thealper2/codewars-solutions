def validate_base(num: str, base: int) -> bool:
    if base < 2 or base > 36:
        return False

    digits = str(num).upper()
    for digit in digits:
        if digit.isdigit():
            value = int(digit)
        else:
            value = ord(digit) - ord("A") + 10
        if value >= base:
            return False

    return True
