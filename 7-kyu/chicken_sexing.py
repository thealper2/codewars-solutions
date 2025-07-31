def correctness(bobs_decisions, expert_decisions):
    points = 0.0
    for bob, expert in zip(bobs_decisions, expert_decisions):
        if bob == expert:
            points += 1.0
        elif bob == "?" or expert == "?":
            points += 0.5
        else:
            continue

    return points
