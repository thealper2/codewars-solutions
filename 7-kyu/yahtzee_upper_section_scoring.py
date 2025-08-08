def yahtzee_upper(dice):
    return max(x * dice.count(x) for x in set(dice))
