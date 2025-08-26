def stem_and_leaf(data):
    plot = {}
    for num in data:
        stem = num // 10
        leaf = num % 10
        if stem not in plot:
            plot[stem] = []
            
        plot[stem].append(leaf)
        
    for stem in plot:
        plot[stem].sort()
        
    return plot
