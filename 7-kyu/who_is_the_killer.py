from collections import defaultdict


def killer(suspect_info, dead):
    n = len(dead)
    suspects = defaultdict(int)
    for k, v in suspect_info.items():
        for person in dead:
            if person in v:
                suspects[k] += 1
                
        if suspects[k] == n:
            return k
        
    return None
