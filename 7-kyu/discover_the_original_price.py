def discover_original_price(discounted_price, sale_percentage):
    return discounted_price + sale_percentage * (
        discounted_price / (100 - sale_percentage)
    )
