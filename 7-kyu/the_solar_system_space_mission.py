from preloaded import fuel_map

def successful_mission(solar_system, destination_planet, fuel):
    earth_idx = solar_system.index("Earth")
    dest_idx = solar_system.index(destination_planet)

    lo, hi = sorted((earth_idx, dest_idx))
    path = solar_system[lo + 1:hi]

    cost = sum(fuel_map[obj] for obj in path)
    cost += 2 * fuel_map[destination_planet]

    return fuel >= cost