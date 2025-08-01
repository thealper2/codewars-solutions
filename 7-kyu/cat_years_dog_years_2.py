def owned_cat_and_dog(cat_years, dog_years):
    owned_cat = 0
    if cat_years < 15:
        owned_cat = 0
    elif 15 <= cat_years < 24:
        owned_cat = 1
    elif cat_years == 24:
        owned_cat = 2
    else:
        owned_cat = 2 + (cat_years - 24) // 4
    
    owned_dog = 0
    if dog_years < 15:
        owned_dog = 0
    elif 15 <= dog_years < 24:
        owned_dog = 1
    elif dog_years == 24:
        owned_dog = 2
    else:
        owned_dog = 2 + (dog_years - 24) // 5
    
    return [owned_cat, owned_dog]
