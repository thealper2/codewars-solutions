def find_outlier(integers):
    evens = [x for x in integers if x % 2 == 0]
    odds = [x for x in integers if x % 2 != 0]
    return odds[0] if len(evens) > 1 else evens[0]