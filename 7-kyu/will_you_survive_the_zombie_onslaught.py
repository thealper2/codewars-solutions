def zombie_shootout(zombies, distance, ammo):
    required = distance * 2
    if zombies <= required and ammo >= zombies:
        return f'You shot all {zombies} zombies.'
    elif zombies <= required and ammo < zombies:
        return f'You shot {ammo} zombies before being eaten: ran out of ammo.'
    elif zombies > required:
        if required > ammo:
            return f'You shot {ammo} zombies before being eaten: ran out of ammo.'
        else:
            return f'You shot {required} zombies before being eaten: overwhelmed.'
