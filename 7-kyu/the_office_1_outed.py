def outed(meet, boss):
    total = 0
    for k, v in meet.items():
        if k == boss:
            total += v * 2
        else:
            total += v
    
    total = total / len(meet)
    return "Nice Work Champ!" if total > 5 else "Get Out Now!"