from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr in ('null', 'NULL', 'nil', 'nullptr', 'null()'):
        return None

    parts = list_repr.split(' -> ')
    values = [int(p) for p in parts[:-1]]
    head = None
    for v in reversed(values):
        head = Node(v, head)

    return head