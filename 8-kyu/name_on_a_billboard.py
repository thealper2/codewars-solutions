def billboard(name, price=30):
    return sum([price for _ in range(len(name))])
