def olympic_ring(string):
    ring_letters = {
        'a': 1, 'b': 1, 'd': 1, 'e': 1, 'g': 1, 'o': 1, 'p': 1, 'q': 1, 
        'A': 1, 'B': 2, 'D': 1, 'O': 1, 'P': 1, 'Q': 1, 'R': 1
    }
    total_rings = 0
    for char in string:
        total_rings += ring_letters.get(char, 0)
        
    score = total_rings // 2
    if score <= 1:
        return 'Not even a medal!'
    elif score == 2:
        return 'Bronze!'
    elif score == 3:
        return 'Silver!'
    else:
        return 'Gold!'
