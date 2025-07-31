def share_price(invested, changes):
    current_value = invested
    for change in changes:
        current_value *= 1 + change / 100

    return "{0:.2f}".format(current_value)
