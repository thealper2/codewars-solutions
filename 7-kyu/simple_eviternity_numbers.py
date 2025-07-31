from itertools import product


def solve(a, b):
    count = 0
    max_length = len(str(b - 1))

    for length in range(1, max_length + 1):
        for digits in product("358", repeat=length):
            num_str = "".join(digits)
            num = int(num_str)
            if a <= num < b:
                c3 = num_str.count("3")
                c5 = num_str.count("5")
                c8 = num_str.count("8")
                if c3 <= c5 <= c8:
                    count += 1
    return count
