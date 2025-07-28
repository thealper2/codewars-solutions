def total_licks(env):
    base_licks = 252
    total = base_licks
    max_increase = 0
    toughest_condition = None
    
    for condition, value in env.items():
        total += value
        if value > max_increase:
            max_increase = value
            toughest_condition = condition
    
    if toughest_condition is not None:
        return f"It took {total} licks to get to the tootsie roll center of a tootsie pop. The toughest challenge was {toughest_condition}."
    else:
        return f"It took {total} licks to get to the tootsie roll center of a tootsie pop."