def draw_stairs(n):
    result = ""
    i = 1
    while i < n:
        result += "I\n"
        result += " " * i
        i += 1

    result += "I"

    return str(result)