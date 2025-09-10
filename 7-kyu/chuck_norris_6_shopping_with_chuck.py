def price(start, soil, age):
    if not isinstance(start, (int, float)) or not isinstance(age, int) or not isinstance(soil, str):
        return 'Chuck is bottomless!'
    
    soil_rates = {
        'Barely used': 10,
        'Seen a few high kicks': 25,
        'Blood stained': 30,
        'Heavily soiled': 50
    }
    
    if soil not in soil_rates:
        return 'Chuck is bottomless!'
    
    rate = soil_rates[soil]
    final_price = start * (1 + rate/100) ** age
    return '${:.2f}'.format(final_price)
