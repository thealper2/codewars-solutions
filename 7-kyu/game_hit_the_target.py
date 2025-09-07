def solution(mtrx):
    for row in mtrx:
        if '>' in row and 'x' in row:
            if row.index('>') < row.index('x'):
                return True
        
    return False
