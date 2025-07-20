def is_information_consistent(evidences):
    return all(
        all(w[d] != 1 for w in evidences) or all(w[d] != -1 for w in evidences)
        for d in range(len(evidences[0])
    ))