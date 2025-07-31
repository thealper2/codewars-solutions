def work_needed(project_minutes, free_lancers):
    total_minutes = 0
    for free_lancer in free_lancers:
        total_minutes += free_lancer[0] * 60 + free_lancer[1]

    if total_minutes >= project_minutes:
        return "Easy Money!"
    else:
        diff = project_minutes - total_minutes
        need_hours = diff // 60
        need_minutes = diff - need_hours * 60
        return f"I need to work {need_hours} hour(s) and {need_minutes} minute(s)"
