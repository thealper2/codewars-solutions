def fuel_price(litres, price_per_litre):
    for i in range(2, 11, 2):
        if litres >= i:
            price_per_litre -= 0.05

    return round(litres * price_per_litre, 2)
