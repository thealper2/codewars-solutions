def slot(st):
    length = len(st)
    if length != 5:
        return 0

    if st == "!!!!!" or st == "?????":
        return 1000

    if "!!!!" in st or "????" in st:
        return 800

    mixed_patterns = {"!!!??", "???!!", "??!!!", "!!???"}
    if st in mixed_patterns:
        return 500

    if "!!!" in st or "???" in st:
        return 300

    complex_patterns = {"!!?!!", "??!??", "!!??!", "??!!?", "!??!!", "?!!??"}
    if st in complex_patterns:
        return 200

    if "!!" in st or "??" in st:
        return 100

    return 0
