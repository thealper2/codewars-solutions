def days_of(items):
    return [f"{(i + 1) * (len(items) - i)} {items[i]}" for i in range(len(items))]
