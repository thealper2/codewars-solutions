def to_currency(price):
    price = str(price)[::-1]
    chunks = [price[i:i+3] for i in range(0, len(price), 3)]
    formatted = ','.join(chunks)[::-1]
    return formatted