def stock_list(stocklist, categories):
    freq = {}
    for stock in stocklist:
        if stock[0] not in freq:
            freq[stock[0]] = int(stock.split(' ')[1])
        else:
            freq[stock[0]] += int(stock.split(' ')[1])
    
    if all(v == 0 for v in freq.values()):
        return ''
    
    result = []
    for category in categories:
        result.append(f"({category} : {freq.get(category, 0)})")
        
    return ' - '.join(result)
