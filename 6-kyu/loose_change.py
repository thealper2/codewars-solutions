def loose_change(cents):
    if cents < 0:
        return {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    
    quarters, remaining = divmod(cents, 25)
    dimes, remaining = divmod(remaining, 10)
    nickels, remaining = divmod(remaining, 5)
    pennies, _ = divmod(remaining, 1)
    
    return {'Nickels': nickels, 'Pennies': pennies, 'Dimes': dimes, 'Quarters': quarters}