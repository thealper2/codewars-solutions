def berlin_clock(time):
    hh, mm, ss = map(int, time.split(':'))
    top = 'Y' if ss % 2 == 0 else 'O'
    hours_5 = hh // 5
    row1 = 'R' * hours_5 + 'O' * (4 - hours_5)
    hours_1 = hh % 5
    row2 = 'R' * hours_1 + 'O' * (4 - hours_1)
    mins_5 = mm // 5
    row3 = ''
    for i in range(11):
        if i < mins_5:
            if (i + 1) % 3 == 0:
                row3 += 'R'
            else:
                row3 += 'Y'    
        else:
            row3 += 'O'
            
    mins_1 = mm % 5
    row4 = 'Y' * mins_1 + 'O' * (4 - mins_1)
    return '\n'.join([top, row1, row2, row3, row4])