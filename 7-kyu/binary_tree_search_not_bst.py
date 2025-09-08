from __future__ import annotations
from typing import Optional


class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right
        
    
def search(n: int, root: Optional[Node]) -> bool:
    stack = [root]
    
    while stack:
        node = stack.pop()
        if node:
            if node.value == n:
                return True

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)
    
    return False
