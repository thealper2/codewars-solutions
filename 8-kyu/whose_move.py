def whose_move(last_player, win):
    if win:
        return last_player
    elif last_player == "black":
        return "white"
    elif last_player == "white":
        return "black"