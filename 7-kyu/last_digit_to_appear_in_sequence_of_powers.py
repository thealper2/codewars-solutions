def ldta(n):
    seen = set()
    counter = 0
    power = 1

    while counter < 100:
        total = n**power
        digits = list(map(int, list(str(total))))

        for digit in digits:
            if digit not in seen:
                if len(seen) == 9:
                    return digit
                else:
                    seen.add(digit)

        counter += 1
        power += 1
