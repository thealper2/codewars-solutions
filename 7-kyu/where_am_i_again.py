class Walker:
    def __init__(self):
        self.xcord = 0
        self.ycord = 0
        
    def walk(self, path):
        for w in path:
            if w == 'e':
                self.xcord += 1
            elif w == 'w':
                self.xcord -= 1
            elif w == 'n':
                self.ycord += 1
            elif w == 's':
                self.ycord -= 1
                
    def coords(self):
        return (self.xcord, self.ycord)
