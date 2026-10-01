def bingo(ticket,win):
    mini_win = 0
    for t in ticket:
        s, n = t
        found = False
        for c in s:
            if ord(c) == n:
                found = True
                break

        if found:
            mini_win += 1

    return 'Winner!' if mini_win >= win else 'Loser!'