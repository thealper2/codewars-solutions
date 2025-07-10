def premier_league_standings(teams):
    if not teams:
        return {}

    champion = teams.get(1)
    other_teams = [team for pos, team in teams.items() if pos != 1]
    other_teams_sorted = sorted(other_teams)
    new_standings = {1: champion}
    for position, team in enumerate(other_teams_sorted, start=2):
        new_standings[position] = team
    
    return new_standings
