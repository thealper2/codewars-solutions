def no_ifs_no_buts(a, b):
    return [
        f"{a} is equal to {b}",
        f"{a} is greater than {b}",
        f"{a} is smaller than {b}",
    ][(a > b) - (a < b)]
