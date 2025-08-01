class Quark(object):
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
        self.baryon_number = 1 / 3
        
    def interact(self, q):
        self.color, q.color = q.color, self.color
    
