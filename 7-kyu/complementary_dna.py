def DNA_strand(dna):
    matches = {"A": "T", "T": "A", "C": "G", "G": "C"}

    return "".join(matches[c] for c in dna)
