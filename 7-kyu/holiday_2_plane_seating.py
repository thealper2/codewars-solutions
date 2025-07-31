def plane_seat(a):
    p1 = p2 = ""

    if int(a[:-1]) <= 20:
        p1 = "Front"
    elif int(a[:-1]) <= 40:
        p1 = "Middle"
    elif int(a[:-1]) <= 60:
        p1 = "Back"
    else:
        return "No Seat!!"

    if ord(a[-1]) <= 67:
        p2 = "Left"
    elif ord(a[-1]) <= 70:
        p2 = "Middle"
    elif ord(a[-1]) <= 72 or ord(a[-1]) == 75:
        p2 = "Right"
    else:
        return "No Seat!!"

    return p1 + "-" + p2
