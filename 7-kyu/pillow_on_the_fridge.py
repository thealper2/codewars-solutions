def pillow(s):
    first_str = s[0]
    second_str = s[1]

    if "n" not in first_str or "B" not in second_str:
        return False

    for i in range(min(len(first_str), len(second_str))):
        if first_str[i] == "n" and second_str[i] == "B":
            return True

    return False
