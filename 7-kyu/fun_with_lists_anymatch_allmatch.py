from typing import Callable, Any

def any_match(head: Node, pred: Callable[[Any], bool]) -> bool:
    current_node = head
    while current_node:
        data = current_node.data
        if pred(data):
            return True
        
        current_node = current_node.next
        
    return False
    
def all_match(head: Node, pred: Callable[[Any], bool]) -> bool:
    current_node = head
    while current_node:
        data = current_node.data
        if not pred(data):
            return False
        
        current_node = current_node.next
        
    return True
