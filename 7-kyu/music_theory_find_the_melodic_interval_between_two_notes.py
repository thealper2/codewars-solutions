def get_interval(note1, note2):
    notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    n1_name, n1_oct = note1[:-1], int(note1[-1])
    n2_name, n2_oct = note2[:-1], int(note2[-1])
    idx1 = notes.index(n1_name)
    idx2 = notes.index(n2_name)
    total1 = n1_oct * 7 + idx1
    total2 = n2_oct * 7 + idx2
    return abs(total2 - total1) + 1
