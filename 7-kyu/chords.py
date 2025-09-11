notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def chords(root):
    idx = notes.index(root)
    major = [notes[idx], notes[(idx + 4) % 12], notes[(idx + 7) % 12]]
    minor = [notes[idx], notes[(idx + 3) % 12], notes[(idx + 7) % 12]]
    return [major, minor]
