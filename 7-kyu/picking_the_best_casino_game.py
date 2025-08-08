def find_best_game(games):
    def expected_value(game):
        return sum(prob * reward for prob, reward in game.outcomes)

    best_game = max(games, key=expected_value)
    return best_game.name
