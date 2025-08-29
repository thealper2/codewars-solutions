class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def add(self, other):
        other.x += self.x
        other.y += self.y
        return other
