def pizza_rewards(customers, min_orders, min_price):
    return {
        name for name, orders in customers.items()
        if sum(1 for o in orders if o >= min_price) >= min_orders
    }