def has_loop(arr: list[int]) -> bool:
    if not arr:
        return False
    
    visited = set()
    current_index = 0
    
    while True:
        if current_index in visited:
            return True
        
        visited.add(current_index)
        next_index = arr[current_index]
        if next_index < 0 or next_index >= len(arr):
            return False
        
        current_index = next_index