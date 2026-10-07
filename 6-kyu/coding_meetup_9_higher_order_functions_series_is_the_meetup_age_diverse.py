def is_age_diverse(lst):
    if len(lst) < 10:
        return False
    
    ages = set()
    for l in lst:
        age = l['age']
        if age >= 100:
            ages.add(100)
        elif age >= 90:
            ages.add(90)
        elif age >= 80:
            ages.add(80)
        elif age >= 70:
            ages.add(70)
        elif age >= 60:
            ages.add(60)
        elif age >= 50:
            ages.add(50)
        elif age >= 40:
            ages.add(40)
        elif age >= 30:
            ages.add(30)
        elif age >= 20:
            ages.add(20)
        elif age >= 10:
            ages.add(10)
            
    return len(ages) == 10