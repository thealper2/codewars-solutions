def rpsls(pl1, pl2):
    rules = {
        'scissors': ['paper', 'lizard'],
        'paper': ['rock', 'spock'],
        'rock': ['lizard', 'scissors'],
        'lizard': ['spock', 'paper'],
        'spock': ['scissors', 'rock']
    }
    
    if pl1 == pl2:
        return 'Draw!'
    elif pl2 in rules[pl1]:
        return 'Player 1 Won!'
    else:
        return 'Player 2 Won!'
