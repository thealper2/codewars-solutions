import math

def raffle_odds(total, purchased):
    lose_num, lose_den = 1, 1
    for total, bought in zip(totals, purchased):
        if total == bought:
            return "1/1"
            
        lose_num *= (total - bought)
        lose_den *= total
        
    win_num = lose_den - lose_num
    win_den = lose_den
    
    g = math.gcd(win_num, win_den)
    win_num //= g
    win_den //= g
    return f"{win_num}/{win_den}"