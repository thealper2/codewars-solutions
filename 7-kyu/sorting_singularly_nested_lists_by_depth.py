def sort_by_depth(arr):
    def get_depth(a):
        depth = 0
        while a == [] or (isinstance(a, list) and len(a) == 1):
            depth += 1
            if a == []:
                break
                
            a = a[0]
            
        return depth
        
    return sorted(arr, key=get_depth)
    
