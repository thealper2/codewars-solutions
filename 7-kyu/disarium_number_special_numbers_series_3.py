def disarium_number(number):
    n = 0
    while 10**n <= number:
        n += 1

    i = 0
    result = 0
    while 10**i <= number:
        d = number // 10**i % 10

        result += d**n
        i += 1
        n -= 1

    return "Disarium !!" if result == number else "Not !!"
