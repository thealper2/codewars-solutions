from collections import defaultdict


def highest_age(group1,group2):
    total_ages = defaultdict(int)
    for person in group1 + group2:
        total_ages[person['name']] += person['age']

    max_age = max(total_ages.values())
    max_names = [name for name, age in total_ages.items() if age == max_age]
    return sorted(max_names)[0]
