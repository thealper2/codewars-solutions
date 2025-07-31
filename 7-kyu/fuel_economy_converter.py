def mpg2lp100km(mpg):
    liters_per_100km = (100 * 3.785411784) / (1.609344 * mpg)
    return round(liters_per_100km, 2)


def lp100km2mpg(lp100km):
    miles_per_gallon = (100 * 3.785411784) / (1.609344 * lp100km)
    return round(miles_per_gallon, 2)
