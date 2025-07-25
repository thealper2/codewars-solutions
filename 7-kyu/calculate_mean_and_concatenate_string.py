def mean(lst):
    total = 0
    n = 0
    string = ''
    
    for item in lst:
        if item.isdigit():
            total += int(item)
            n += 1
        else:
            string += item
            
    return [total / n, string]