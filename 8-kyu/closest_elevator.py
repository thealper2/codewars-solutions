def elevator(left, right, call):
    a = abs(call - left)
    b = abs(call - right)
    if a > b:
        return "right"
    elif a < b:
        return "left"
    else:
        return "right"