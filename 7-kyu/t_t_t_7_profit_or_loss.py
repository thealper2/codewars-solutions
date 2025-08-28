def profit_loss(records):
    total_cost = 0
    total_sale = 0
    for sale in records:
        price, percent = sale
        total_sale += price
        cost = price / (1 + percent / 100)
        total_cost += cost
        
    result = total_sale - total_cost
    return round(result, 2)
