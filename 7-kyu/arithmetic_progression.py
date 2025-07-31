def arithmetic_sequence_elements(a, d, n):
    sequence = [a + i * d for i in range(n)]
    return ", ".join(map(str, sequence))
