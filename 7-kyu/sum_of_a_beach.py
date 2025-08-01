def sum_of_a_beach(beach):
    beach = beach.lower()
    sand = beach.count('sand')
    water = beach.count('water')
    fish = beach.count('fish')
    sun = beach.count('sun')
    return sand + water + fish + sun
