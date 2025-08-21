def stone_pick(arr):
    items = {}
    for item in arr:
        if item not in items:
            items[item] = 1
        else:
            items[item] += 1
    
    
    return min(
        items.get('Cobblestone', 0) // 3,
        (items.get('Wood', 0) * 4 + items.get('Sticks', 0)) // 2
    )
