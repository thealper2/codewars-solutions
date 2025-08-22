class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def append(listA, listB):
    if not listA:
        return listB
    if not listB:
        return listA
        
    current = listA
    while current.next:
        current = current.next
        
    current.next = listB
    return listA
