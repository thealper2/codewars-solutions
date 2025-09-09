def death_star(week, attack):
    required = [100, 75, 50]
    total = [0, 0, 0]
    for day in range(attack):
        shipment = week[day]
        for i in range(3):
            total[i] += shipment[i]
    if total[0] >= required[0] and total[1] >= required[1] and total[2] >= required[2]:
        return "The station is completed!"
    else:
        iron_needed = max(0, required[0] - total[0])
        steel_needed = max(0, required[1] - total[1])
        chromium_needed = max(0, required[2] - total[2])
        return f"The station is destroyed! It needed {iron_needed} iron, {steel_needed} steel and {chromium_needed} chromium for completion."
