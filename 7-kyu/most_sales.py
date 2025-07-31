def top3(products, amounts, prices):
    n = len(products)
    sales = []
    for i in range(n):
        sales.append((products[i], amounts[i] * prices[i], i))

    sales.sort(key=lambda x: (-x[1], x[2]))
    return [product for product, total, index in sales[:3]]
