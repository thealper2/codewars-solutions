def make_change(amount):
    if amount == 0:
        return {}
    
    coins = [('H', 50), ('Q', 25), ('D', 10), ('N', 5), ('P', 1)]
    result = {}
    
    for symbol, value in coins:
        count, amount = divmod(amount, value)
        if count:
            result[symbol] = count
            
    return result
