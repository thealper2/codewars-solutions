def change_me(money):
    accepted_values = {
        "£5": 500,
        "£2": 200,
        "£1": 100,
        "50p": 50,
        "20p": 20
    }

    if money not in accepted_values:
        return money
    
    amount = accepted_values[money]
    result = []
    
    if amount == 20:
        return "10p 10p"

    while amount >= 20:
        result.append("20p")
        amount -= 20
    
    while amount >= 10:
        result.append("10p")
        amount -= 10
    
    return " ".join(result)