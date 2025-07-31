def next_letter(s):
    result = []
    for char in s:
        if char.isalpha():
            if char == "z":
                next_char = "a"
            elif char == "Z":
                next_char = "A"
            else:
                next_char = chr(ord(char) + 1)
            result.append(next_char)
        else:
            result.append(char)

    return "".join(result)
