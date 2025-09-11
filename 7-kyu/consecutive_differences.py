def differences(lst):
    while len(lst) > 1:
        lst = [abs(lst[i + 1] - lst[i]) for i in range(len(lst) - 1)]
        
    return lst[0]
