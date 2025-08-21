def solve(alice, bob):
    alice_points = sum(1 for a, b in zip(alice, bob) if a > b)
    bob_points = sum(1 for a, b in zip(alice, bob) if b > a)
    
    if alice_points > bob_points:
        message = 'Alice made "Kurt" proud!'
    elif bob_points > alice_points:
        message = 'Bob made "Jeff" proud!'
    else:
        message = 'that looks like a "draw"! Rock on!'
    
    return f'{alice_points}, {bob_points}: {message}'
