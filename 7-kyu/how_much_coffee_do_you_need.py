def how_much_coffee(events):
    coffee = 0
    d = {
        "cw": 1,
        "cat": 1,
        "dog": 1,
        "movie": 1,
        "CW": 2,
        "CAT": 2,
        "DOG": 2,
        "MOVIE": 2
    }

    for event in events:
        coffee += d.get(event, 0)
        
        if coffee > 3:
            return "You need extra sleep"
        
    return coffee
