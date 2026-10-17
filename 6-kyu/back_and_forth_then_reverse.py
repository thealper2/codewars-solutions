from collections import deque

def arrange(s):
    dq = deque(s)
    t = []
    reverse = False
    
    while dq:
        if not reverse:
            t.append(dq.popleft())
            if dq:
                t.append(dq.pop())
        else:
            t.append(dq.pop())
            if dq:
                t.append(dq.popleft())
                
        reverse = not reverse
        
    return t