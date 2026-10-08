class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_nth(head, index, data):
    if index < 0:
        raise IndexError('Invalid index')

    new_node = Node(data)

    if index == 0:
        new_node.next = head
        return new_node

    current = head
    i = 0
    while current is not None and i < index - 1:
        current = current.next
        i += 1

    if current is None:
        raise IndexError('Invalid index')

    new_node.next = current.next
    current.next = new_node
    return head