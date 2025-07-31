def calculate_total(subtotal, tax, tip):
    tax_amount = subtotal * (tax / 100)
    tip_amount = subtotal * (tip / 100)
    total = subtotal + tax_amount + tip_amount
    return round(total, 2)
