from collections import defaultdict


def count_vegetables(string):
    valid_vegetables = {"cabbage", "carrot", "celery", "cucumber", "mushroom", "onion", "pepper", "potato", "tofu", "turnip"}
    vegetable_counts = defaultdict(int)
    vegetables = string.split()
    
    for veg in vegetables:
        if veg in valid_vegetables:
            vegetable_counts[veg] += 1
    
    count_list = [(count, veg) for veg, count in vegetable_counts.items()]
    count_list.sort(key=lambda x: x[1], reverse=True)
    count_list.sort(key=lambda x: x[0], reverse=True)
    return count_list