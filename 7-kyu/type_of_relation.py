def type_of_function(domain, codomain, relations):
    domain_to_codomain = {}
    for x, y in relations:
        if x in domain_to_codomain:
            if domain_to_codomain[x] != y:
                return "It is not a function"
        else:
            domain_to_codomain[x] = y

    if set(domain_to_codomain.keys()) != domain:
        return "It is not a function"

    codomain_elements = set()
    injective = True
    for y in domain_to_codomain.values():
        if y in codomain_elements:
            injective = False
            break
        codomain_elements.add(y)

    surjective = set(domain_to_codomain.values()) == codomain

    if injective and surjective:
        return "Bijective"
    elif injective:
        return "Injective"
    elif surjective:
        return "Surjective"
    else:
        return "General function"
