def sort_animals(lst : list) -> list:
    return sorted(lst, key=lambda a: (a.number_of_legs, a.name))