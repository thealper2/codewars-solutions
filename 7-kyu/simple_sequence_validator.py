def validate_sequence(sequence):
    p = sequence[1] - sequence[0]
    n = len(sequence)
    for i in range(1, n - 1):
        if sequence[i + 1] - sequence[i] != p:
            return False
        
    return True
