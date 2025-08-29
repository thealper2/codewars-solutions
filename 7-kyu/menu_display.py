class Menu:
    def __init__(self, items, cursor=0):
        self.items = items
        self.cursor = cursor
        
    def to_the_right(self):
        self.cursor = (self.cursor + 1) % len(self.items)
        
    def to_the_left(self):
        self.cursor = (self.cursor - 1) % len(self.items)
        
    def display(self):
        result = []
        for i, item in enumerate(self.items):
            if i == self.cursor:
                result.append(f"['{item}']")
            else:
                result.append(f"'{item}'")
                
        return '[' + ', '.join(result) + ']'
