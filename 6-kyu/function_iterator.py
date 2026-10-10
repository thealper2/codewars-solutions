def create_iterator(func, n):
    def iterator(x):
        for _ in range(n):
            x = func(x)
            
        return x
    
    return iterator
