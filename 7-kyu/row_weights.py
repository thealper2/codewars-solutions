def row_weights(array):
    team1 = 0
    team2 = 0
    for index, weight in enumerate(array):
        if index % 2 == 0:
            team1 += weight
        else:
            team2 += weight
            
    return (team1, team2)