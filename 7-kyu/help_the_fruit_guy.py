def remove_rotten(bag_of_fruits):
    if not bag_of_fruits:
        return []
    
    n = len(bag_of_fruits)
    for i in range(n):
        bag_of_fruits[i] = bag_of_fruits[i].replace('rotten', '').lower()
        
    return bag_of_fruits