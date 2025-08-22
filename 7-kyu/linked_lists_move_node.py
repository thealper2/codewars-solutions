class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    if source is None:
        raise ValueError("Source list is empty")
        
    moved_node = source
    new_source = source.next
    moved_node.next = dest
    new_dest = moved_node
    return Context(new_source, new_dest)
