def get_day(day, is_leap):
    months = [
        ("January", 31),
        ("February", 29 if is_leap else 28),
        ("March", 31),
        ("April", 30),
        ("May", 31),
        ("June", 30),
        ("July", 31),
        ("August", 31),
        ("September", 30),
        ("October", 31),
        ("November", 30),
        ("December", 31),
    ]

    for name, days in months:
        if day <= days:
            return f"{name}, {day}"

        day -= days