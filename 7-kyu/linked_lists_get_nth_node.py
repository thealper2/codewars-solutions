from preloaded import Node

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def get_nth(node, index):
    if not node:
        raise Errror("None linked list should throw error.")
    
    count = 0
    while node:
        if count == index:
            return node    
        else:
            count += 1
            node = node.next
            
    raise Error("Invalid index value should throw error.")
            
