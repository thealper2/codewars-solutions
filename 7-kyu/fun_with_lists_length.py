def length(head): 
    size = 0
    current = head
    while current:
        size += 1
        current = current.next
        
    return size
