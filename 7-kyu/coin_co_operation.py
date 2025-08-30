def get_coin_balances(lst1, lst2):
    p1 = 3
    p2 = 3
    for l1, l2 in zip(lst1, lst2):
        if l1 == 'share' and l2 == 'share':
            p1 += 2
            p2 += 2
        elif l1 == 'steal' and l2 == 'share':
            p1 += 3
            p2 -= 1
        elif l1 == 'share' and l2 == 'steal':
            p1 -= 1
            p2 += 3
            
    return (p1, p2)
