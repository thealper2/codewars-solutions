def number_of_folds(n):
    if n <= 1:
        return 0
    
    folds = 0
    while n > 1:
        n = (n + 1) // 2
        folds += 1
        
    return folds