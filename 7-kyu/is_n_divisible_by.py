def is_divisible(n, *args):
    numbers = list(args)
    for number in numbers:
        if n % number != 0:
            return False

    return True
