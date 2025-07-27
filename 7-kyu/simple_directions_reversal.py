def solve(arr):
    if not arr:
        return []
    
    roads = []
    turns = []
    
    for step in arr:
        parts = step.split(' on ')
        if parts[0] == 'Begin':
            roads.append(parts[1])
        else:
            turns.append(parts[0])
            roads.append(parts[1])
            
    reversed_roads = roads[::-1]
    reversed_turns = ['Left' if turn == 'Right' else 'Right' for turn in turns[::-1]]
    
    reversed_arr = [f"Begin on {reversed_roads[0]}"]
    for i in range(1, len(reversed_roads)):
        reversed_arr.append(f"{reversed_turns[i - 1]} on {reversed_roads[i]}")
        
    return reversed_arr