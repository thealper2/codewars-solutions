def tax_calculator(amount):
    if not isinstance(amount, (int, float)) or amount <= 0:
        return 0
    
    tax = 0
    if amount > 30:
        tax += (amount - 30) * 0.03
        amount = 30
        
    if amount > 20:
        tax += (amount - 20) * 0.05
        amount = 20
        
    if amount > 10:
        tax += (amount - 10) * 0.07
        amount = 10
        
    tax += amount * 0.10
    return round(tax, 2)
