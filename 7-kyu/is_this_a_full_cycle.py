def full_cycle(lst):
    n = len(lst)
    visited = set()
    index = 0
    
    for _ in range(n):
        if index in visited:
            return False
        
        visited.add(index)
        index = lst[index]
        
    return index == 0
