def balance_statement(lst):
    if not lst or not lst.strip():
        return "Buy: 0 Sell: 0"

    orders = [o.strip() for o in lst.split(',')]
    buy = 0.0
    sell = 0.0
    bad = []

    for order in orders:
        parts = order.split()
        valid = (
            len(parts) == 4
            and parts[1].lstrip('-').isdigit()
            and '.' in parts[2]
            and _is_float(parts[2])
            and parts[3] in ('B', 'S')
        )
        if not valid:
            bad.append(order)
            continue
        quote, qty, price, status = parts
        total = int(qty) * float(price)
        if status == 'B':
            buy += total
        else:
            sell += total

    result = f"Buy: {round(buy):.0f} Sell: {round(sell):.0f}"
    if bad:
        result += f"; Badly formed {len(bad)}: "
        result += ' ;'.join(bad) + ' ;'
    return result


def _is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False