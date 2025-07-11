def get_animals_count(legs_number, heads_number, horns_number):
    cows = horns_number // 2
    remaining_heads = heads_number - cows
    remaining_legs = legs_number - 4 * cows
    rabbits = (remaining_legs - 2 * remaining_heads) // 2
    chickens = remaining_heads - rabbits
    return {"rabbits": rabbits, "chickens": chickens, "cows": cows}
