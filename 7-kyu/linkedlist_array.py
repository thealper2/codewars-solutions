def list_to_array(node):
    result = []
    
    while node:
        result.append(node.value)
        node = node.next
        
    return result