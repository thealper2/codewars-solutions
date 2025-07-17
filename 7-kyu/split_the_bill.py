def split_the_bill(x):
    mean = sum(x.values()) / len(x)
    pay = {}
    for k, v in x.items():
        pay[k] = round(v - mean, 2)
        
    return pay
