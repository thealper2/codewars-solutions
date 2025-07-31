def martingale(bank, outcomes):
    if not outcomes:
        return bank

    stake = 100
    for outcome in outcomes:
        if outcome == 0:
            bank -= stake
            stake *= 2
        elif outcome == 1:
            bank += stake
            stake = 100

    return bank
