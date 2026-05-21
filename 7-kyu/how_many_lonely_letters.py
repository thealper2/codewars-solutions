from collections import Counter

def count_lonely_letters(text):
    letters = [ch.lower() for ch in text if ch.isalpha()]
    freq = Counter(letters)
    present = set(freq.keys())
    lonely_count = 0
    for letter, count in freq.items():
        if count == 1:
            neighbors = []
            if letter > 'a':
                neighbors.append(chr(ord(letter) - 1))
            
            if letter < 'z':
                neighbors.append(chr(ord(letter) + 1))
                
            if not any(neighbor in present for neighbor in neighbors):
                lonely_count += 1
                
    return lonely_count