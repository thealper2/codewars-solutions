def next_day_of_week(current_day, available_week_days):
    binary_representation = bin(available_week_days)[2:].zfill(7)
    binary_representation = binary_representation[::-1]

    i = current_day + 1
    while True:
        if i > 7:
            i = 1

        if binary_representation[i - 1] == "1":
            return i

        i += 1
