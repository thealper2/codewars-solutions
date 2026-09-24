def check_valid_tr_number(number):
    if isinstance(number, bool):
        return False
    if not isinstance(number, (int, str)):
        return False

    s = str(number)
    if not s.isdigit():
        return False
    if len(s) != 11:
        return False
    if s[0] == '0':
        return False

    digits = [int(c) for c in s]

    odd_sum = digits[0] + digits[2] + digits[4] + digits[6] + digits[8]
    even_sum = digits[1] + digits[3] + digits[5] + digits[7]

    if (odd_sum * 7 - even_sum) % 10 != digits[9]:
        return False

    if sum(digits[:10]) % 10 != digits[10]:
        return False

    return True
