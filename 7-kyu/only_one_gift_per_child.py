seen = set()

def hand_out_gift(name):
    if name in seen:
        raise ValueError("Child already received a gift")
        
    seen.add(name)
