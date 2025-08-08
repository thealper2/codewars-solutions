def race(speed1, speed2, distance, sleep, getup):
    time_hare_run_before_sleep = sleep / speed1
    tortoise_pos_when_hare_sleeps = speed2 * time_hare_run_before_sleep
    tortoise_sleep_distance = (distance - getup) - tortoise_pos_when_hare_sleeps
    hare_sleep_time = tortoise_sleep_distance / speed2
    hare_remaining_distance = distance - sleep
    time_hare_run_after_sleep = hare_remaining_distance / speed1
    tortoise_remaining_distance = speed2 * time_hare_run_after_sleep
    tortoise_final_pos = (distance - getup) + tortoise_remaining_distance
    hare_finish_time = time_hare_run_before_sleep + hare_sleep_time + time_hare_run_after_sleep
    tortoise_finish_time = distance / speed2

    if abs(hare_finish_time - tortoise_finish_time) < 1e-9:
        winner_str = "The hare and the tortoise tied."
        sleep_str = f"The hare is sleeping for {round(hare_sleep_time)} minutes."
    elif hare_finish_time < tortoise_finish_time:
        winner_str = "The hare won the race. He is sleeping for " + str(round(hare_sleep_time)) + " minutes."
        return winner_str
    else:
        winner_str = "The tortoise won the race. The hare is sleeping for " + str(round(hare_sleep_time)) + " minutes."
        return winner_str

    return f"{winner_str} {sleep_str}"
