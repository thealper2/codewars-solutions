def code_for_same_protein(dna1, dna2):
    return all(
        codons[dna1[i : i + 3]] == codons[dna2[i : i + 3]]
        for i in range(0, len(dna1), 3)
    )
