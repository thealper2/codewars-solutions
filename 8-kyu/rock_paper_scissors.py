def rps(p1, p2):
    if p1 == p2:
        return "Draw!"

    cases = [("scissors", "paper"), ("paper", "rock"), ("rock", "scissors")]

    if (p1, p2) in cases:
        return "Player 1 won!"
    elif (p2, p1) in cases:
        return "Player 2 won!"
