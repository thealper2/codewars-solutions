def aa_percentage(sequence, residues=None):
    if residues is None:
        residues = ["A", "I", "L", "M", "F", "W", "Y", "V"]
    
    total = len(sequence)
    if total == 0:
        return 0
    
    count = sum(1 for aa in sequence if aa in residues)
    percentage = (count / total) * 100
    return round(percentage)
