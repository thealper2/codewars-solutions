def get_average(lst): 
    s = sum([item['age'] for item in lst])
    avg = s / len(lst)
    return round(avg)
