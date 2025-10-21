class DefaultList:
    def __init__(self, lst, default):
        self.lst = lst[:]
        self.default = default
        
    def __getitem__(self, index):
        try:
            return self.lst[index]
        except IndexError:
            return self.default
        
    def __setitem__(self, index, value):
        if 0 <= index < len(self.lst) or -len(self.lst) <= index < 0:
            self.lst[index] = value
        else:
            raise IndexError('')
            
    def extend(self, iterable):
        self.lst.extend(iterable)
        
    def append(self, item):
        self.lst.append(item)
        
    def insert(self, index, item):
        self.lst.insert(index, item)
        
    def remove(self, item):
        self.lst.remove(item)
        
    def pop(self, index=-1):
        return self.lst.pop(index)
    
    def __len__(self):
        return len(self.lst)
    
    def __repr__(self):
        return repr(self.lst)
