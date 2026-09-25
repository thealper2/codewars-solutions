def get_total_cash_prize(prize_fund, correct_answers, player_actions):
    cash = 0
    safe = 0
    lifelines_used = 0

    for i, action in enumerate(player_actions):
        j = 0
        while j < len(action) and action[j] in "123":
            lifelines_used += 1
            j += 1

        final = action[j:]

        if final == 'W':
            return [cash, lifelines_used]

        if final == 'X':
            return [safe, lifelines_used]

        if final == correct_answers[i]:
            cash += prize_fund[i]
            if (i + 1) % 5 == 0:
                safe = cash
        else:
            return [0, lifelines_used]

    return [cash, lifelines_used]