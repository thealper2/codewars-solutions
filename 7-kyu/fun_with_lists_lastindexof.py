def last_index_of(head, search_val):
    current = head
    idx = 0
    result = -1
    while current:
        if current.data == search_val:
            result = idx
        
        idx += 1
        current = current.next
        
    return result
