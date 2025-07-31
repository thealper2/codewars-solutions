def day_plan(hours, tasks, duration):
    total_available_minutes = hours * 60
    total_work_time = tasks * duration

    if total_work_time > total_available_minutes:
        return "You're not sleeping tonight!"

    if tasks == 0:
        return []

    if tasks == 1:
        return [duration]

    total_break_time = total_available_minutes - total_work_time
    number_of_breaks = tasks - 1
    break_duration = (
        round(total_break_time / number_of_breaks) if number_of_breaks != 0 else 0
    )

    schedule = []
    for i in range(tasks):
        schedule.append(duration)
        if i < number_of_breaks:
            schedule.append(break_duration)

    return schedule
