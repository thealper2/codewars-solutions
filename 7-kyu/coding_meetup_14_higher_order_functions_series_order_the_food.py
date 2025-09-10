from collections import defaultdict 


def order_food(lst): 
    food = defaultdict(int)
    for item in lst:
        f = item['meal']
        food[f] += 1
        
    return food
