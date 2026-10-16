def sort_string(s, ordering):
    seen = set()
    order = []
    for c in ordering:
        if c not in seen:
            seen.add(c)
            order.append(c)
    
    order_index = {c: i for i, c in enumerate(order)}
    in_order = sorted((c for c in s if c in order_index), key=lambda c: order_index[c])
    not_in_order = [c for c in s if c not in order_index]
    return ''.join(in_order) + ''.join(not_in_order)