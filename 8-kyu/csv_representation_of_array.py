def to_csv_text(array):
    sequences = []
    for row in array:
        sequence = ",".join([str(item) for item in row])
        sequences.append(sequence)

    return "\n".join(sequences)