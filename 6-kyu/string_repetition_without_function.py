class str_repeat:
    def __init__(self, s, n):
        self.value = s * n
    
    def __eq__(self, other):
        return self.value == other
