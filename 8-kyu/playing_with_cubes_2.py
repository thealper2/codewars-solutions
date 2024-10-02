class Cube:
    def __init__(self, side=0):
        self.side = abs(side)
    
    def get_side(self):
        """Return the side of the Cube"""
        return self.side

    def set_side(self, new_side):
        """Set the value of the Cube's side."""
        self.side = abs(new_side)
