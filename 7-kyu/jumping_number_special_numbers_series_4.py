def jumping_number(number):
    i = 0
    prev = None
    while 10**i <= number:
        d = number // 10**i % 10
        if prev is not None and abs(d - prev) != 1:
            return "Not!!"

        prev = d
        i += 1

    return "Jumping!!"
