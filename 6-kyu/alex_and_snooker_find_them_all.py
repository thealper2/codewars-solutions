def score(ball: Ball) -> int:
    current = ball
    while current.previous is not None:
        current = current.previous
        
    total = 0
    while current is not None:
        total += current.point
        current = current.next
        
    return total
