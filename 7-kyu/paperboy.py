def cheapest_quote(n):
    bundle_40 = n // 40
    remaining = n % 40
    bundle_20 = remaining // 20
    remaining = remaining % 20
    bundle_10 = remaining // 10
    remaining = remaining % 10
    bundle_5 = remaining // 5
    remaining = remaining % 5
    bundle_1 = remaining

    total_cost = (
        bundle_40 * 3.85
        + bundle_20 * 1.93
        + bundle_10 * 0.97
        + bundle_5 * 0.49
        + bundle_1 * 0.10
    )
    return round(total_cost, 2)
