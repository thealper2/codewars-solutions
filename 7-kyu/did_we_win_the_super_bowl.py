def did_we_win(plays):
    n = len(plays)
    yards = 0

    for i in range(n):
        if plays[i] == []:
            continue
        
        if plays[i][1] == 'turnover':
            return False
        
        if plays[i][1] in ['run', 'pass']:
            yards += plays[i][0]
        
        else:
            yards -= plays[i][0]
    
    if yards > 10:
        return True
    
    return False
