import random

def get_bingo_card():
    card = []
    
    columns = [
        ('B', 1, 15, 5),
        ('I', 16, 30, 5),
        ('N', 31, 45, 4),
        ('G', 46, 60, 5),
        ('O', 61, 75, 5)
    ]
    
    for letter, start, end, count in columns:
        numbers = random.sample(range(start, end + 1), count)
        card.extend(f'{letter}{n}' for n in numbers)
        
    return card