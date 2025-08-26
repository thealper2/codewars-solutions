import random


def actually_really_good(foods):
    a = "You know what's actually really good? "
    if not foods:
        return a + "Nothing!"
    
    if len(foods) == 1:
        food = foods[0].capitalize()
        return a + f'{food} and more {food.lower()}.'
    
    first = random.choice(foods)
    second = random.choice([f for f in foods if f != first]).lower()
    return a + f'{first.capitalize()} and {second}.'
