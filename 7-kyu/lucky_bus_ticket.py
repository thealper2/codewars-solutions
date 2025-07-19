def is_lucky(ticket):
    if not ticket.isdigit():
        return False
    
    if len(ticket) != 6:
        return False
    
    a = list(map(int, list(ticket[:3])))
    b = list(map(int, list(ticket[3:])))
    if sum(a) != sum(b):
        return False
    
    return True