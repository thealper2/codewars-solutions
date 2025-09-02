from preloaded import Hero

def move(self, direction):
    row = int(self.position[0])
    col = int(self.position[1])
    if direction == 'up':
        row -= 1
    elif direction == 'down':
        row += 1
    elif direction == 'left':
        col -= 1
    elif direction == 'right':
        col += 1
    
    if row < 0 or row > 4 or col < 0 or col > 4:
        raise ValueError("Invalid move")
        
    self.position = f"{row}{col}"
    
Hero.move = move
