def nba_extrap(ppg, mpg):
    if ppg == 0 or mpg == 0:
        return 0

    return round(48 * (ppg / mpg), 1)
