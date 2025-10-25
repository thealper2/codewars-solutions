import math

def union_jack(n):
    if not isinstance(n, (int, float)):
        return False
    
    n = max(7, math.ceil(n))
    is_odd = n % 2 == 1
    center = n // 2
    flag = []
    for i in range(n):
        row = []
        for j in range(n):
            main_diag = (i == j)
            anti_diag = (i + j == n - 1)
            if is_odd:
                vertical = (j == center)
                horizontal = (i == center)
            else:
                vertical = (j == center) or (j == center - 1)
                horizontal = (i == center) or (i == center - 1)
            
            if main_diag or anti_diag or vertical or horizontal:
                row.append('X')
            else:
                row.append('-')
                
        flag.append(''.join(row))
    
    return '\n'.join(flag)
