from preloaded import atomic_masses

def count_the_moles(mass_of_substance, chemical_formula):
    total_mass = 0
    i = 0
    n = len(chemical_formula)
    while i < n:
        element = chemical_formula[i]
        i += 1
        count_str = ''
        while i < n and chemical_formula[i].isdigit():
            count_str += chemical_formula[i]
            i += 1
        count = int(count_str) if count_str else 1
        total_mass += atomic_masses[element] * count
    return mass_of_substance / total_mass
