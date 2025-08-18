import math


def cooking_time(needed_power, minutes, seconds, power):
    needed_power = int(needed_power[:-1])
    power = int(power[:-1])
    total_seconds = minutes * 60 + seconds
    adjusted_seconds = (needed_power / power) * total_seconds
    adjusted_seconds = math.ceil(adjusted_seconds)
    adjusted_minutes = adjusted_seconds //  60
    remaining_seconds = adjusted_seconds % 60
    return f"{adjusted_minutes} minutes {remaining_seconds} seconds"
