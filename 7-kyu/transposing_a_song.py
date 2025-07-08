def transpose(song, interval):
    notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    notate = {
        'Bb': 'A#',
        'Db': 'C#',
        'Eb': 'D#',
        'Gb': 'F#',
        'Ab': 'G#'
    }
    result = []
    
    for note in song:
        new_note = notate.get(note, note)
        note_idx = notes.index(new_note)
        result.append(notes[(note_idx + interval) % len(notes)])
        
    return result