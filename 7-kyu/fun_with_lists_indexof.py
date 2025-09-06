def index_of(head, value): 
    current = head
    idx = 0
    while current:
        if current.data == value:
            return idx
        
        idx += 1
        current = current.next
        
    return -1
