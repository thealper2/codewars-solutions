def middle_me(N, X, Y): 
    if N % 2 == 1:
        return X
    
    mid = N // 2
    return mid * Y + X + mid * Y
