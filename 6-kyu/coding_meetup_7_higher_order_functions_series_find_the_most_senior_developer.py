def find_senior(lst): 
    max_age = max(l['age'] for l in lst)
    return [l for l in lst if l['age'] == max_age]