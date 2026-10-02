def get_order(order):
    menu = ["Burger", "Fries", "Chicken", "Pizza", "Sandwich",
            "Onionrings", "Milkshake", "Coke"]
    result = []
    for item in menu:
        count = order.lower().count(item.lower())
        result.extend([item] * count)
    return ' '.join(result)