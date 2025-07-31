def league_calculate(team1, team2, result, league_table):
    if result == "win":
        points1, points2 = 3, 0
    elif result == "draw":
        points1 = points2 = 1
    else:
        points1 = points2 = 0

    for team in league_table:
        if team[0] == team1:
            team[1] += points1
        if team[0] == team2:
            team[1] += points2

    league_table.sort(key=lambda x: (-x[1], x[0]))
    return league_table
