class CircularList():
    def __init__(self, *args):
        if not args:
            raise ValueError("CircularList must have at least one element")
        self.arr = list(args)
        self.idx = -1
            
    def next(self):
        if not self.arr:
            raise ValueError("List is empty")
        
        self.idx += 1
        if self.idx >= len(self.arr):
            self.idx = 0
        
        return self.arr[self.idx]
    
    def prev(self):
        if not self.arr:
            raise ValueError("List is empty")
        
        self.idx -= 1
        if self.idx < 0:
            self.idx = len(self.arr) - 1
        
        return self.arr[self.idx]
