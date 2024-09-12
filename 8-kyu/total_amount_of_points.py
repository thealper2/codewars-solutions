def points(games):
    points = 0
    for game in games:
        home = game[0]
        away = game[2]
        if home > away:
            points += 3
        elif home == away:
            points += 1

    return points