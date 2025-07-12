def get_note(pitch):
    while pitch < 440:
        pitch *= 2;
        
    while pitch > 830.61:
        pitch /= 2;
    
    return notes_dictionary[pitch];