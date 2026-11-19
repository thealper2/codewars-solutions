def arpeggio(note: str) -> list[str] | None:
    notes = ["A", "B", "C", "D", "E", "F", "G"]
    if note not in notes:
        return None

    i = notes.index(note)
    scale = [notes[(i + k) % 7] for k in range(7)]
    return [scale[0], scale[2], scale[4], scale[0]]