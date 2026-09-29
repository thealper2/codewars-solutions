def delete_nth(order,max_e):
    freq = {}
    result = []
    for item in order:
        freq[item] = freq.get(item, 0) + 1
        if freq[item] <= max_e:
            result.append(item)
            
    return result