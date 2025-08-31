def find_max(root):
    max_val = float('-inf')
    stack = [root]
    while stack:
        node = stack.pop()
        max_val = max(max_val, node.value)
        
        if node.left:
            stack.append(node.left)
    
        if node.right:
            stack.append(node.right)
    
    return max_val
