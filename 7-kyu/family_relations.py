def relations(family_list, target_pair):
    parents = {}
    for parent, child in family_list:
        parents[child] = parent

    a, b = target_pair
    a_parent = parents.get(a)
    a_parent_parent = parents.get(a_parent)
    b_parent = parents.get(b)
    b_parent_parent = parents.get(b_parent)

    if b == a_parent:
        return "Mother"

    if b == a_parent_parent:
        return "Grandmother"
    if a == b_parent:
        return "Daughter"
    if a == b_parent_parent:
        return "Granddaughter"
    if a_parent == b_parent:
        return "Sister"
    if a_parent_parent == b_parent_parent:
        return "Cousin"
    if a_parent_parent == b_parent:
        return "Aunt"
    if a_parent == b_parent_parent:
        return "Niece"
