def do_they_agree(alice, bob):
    position = {emp_id: idx for idx, emp_id in enumerate(bob)}
    
    positions = []
    for emp_id in alice:
        if emp_id in position:
            positions.append(position[emp_id])
    
    if len(positions) <= 1:
        return True
    
    for i in range(len(positions) - 1):
        if positions[i] >= positions[i + 1]:
            return False
    
    return True
