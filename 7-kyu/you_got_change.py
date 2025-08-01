def give_change(amount): 
    denominations = [100, 50, 20, 10, 5, 1]
    n = len(denominations)
    result = [0] * 6
    
    for i in range(n):
        bill = denominations[i]
        if amount >= bill:
            count = amount // bill
            result[5 - i] = count
            amount -= count * bill
    
    return tuple(result)
