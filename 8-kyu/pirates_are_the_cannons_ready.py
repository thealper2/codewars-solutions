def cannons_ready(gunners):
    for value in gunners.values():
        if value == "nay":
            return "Shiver me timbers!"
        
    return "Fire!"