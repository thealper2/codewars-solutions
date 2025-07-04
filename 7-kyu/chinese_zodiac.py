from preloaded import animals, elements


def chinese_zodiac(year):
    base_year = 1984
    animal_cycle = 12
    element_cycle = 10
    offset = year - base_year
    animal_index = (offset % animal_cycle + animal_cycle) % animal_cycle
    element_offset = offset % element_cycle
    element_index = (element_offset // 2) % len(elements)
    animal = animals[animal_index]
    element = elements[element_index]
    return f"{element} {animal}"
