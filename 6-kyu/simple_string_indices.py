def solve(st, idx):
    if st[idx] != '(':
        return -1
    
    balance = 0
    for i in range(idx, len(st)):
        if st[i] == '(':
            balance += 1
            
        elif st[i] == ')':
            balance -= 1
            if not balance:
                return i
            
    return -1
        
