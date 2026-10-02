from preloaded import Node

# Node is defined in preloaded:
# class Node:
#     def __init__(self, data):
#        self.data = data
#        self.next = None

def length(node: Node | None) -> int:
    if not node:
        return 0

    current_node = node
    l = 1
    while current_node.next is not None:
        l += 1
        current_node = current_node.next

    return l

def count(node: Node | None, data) -> int:
    if not node:
        return 0

    c = 0
    current_node = node
    while current_node is not None:
        if current_node.data == data:
            c += 1

        current_node = current_node.next

    return c