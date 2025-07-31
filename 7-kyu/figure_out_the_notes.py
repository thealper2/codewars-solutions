def what_note(string, fret):
    notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    index = notes.index(string.upper())
    return notes[(index + fret) % 12]
