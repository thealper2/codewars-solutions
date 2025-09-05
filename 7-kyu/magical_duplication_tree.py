def magic_plant(p_field,split,n):
    lines = p_field.split('\n')
    height = len(lines)
    width = len(lines[0])
    
    for _ in range(n):
        lines = lines[1:]
        lines = [line * split for line in lines]
        width *= split
        height -= 1
        if height == 0:
            break
            
    if lines:
        lines[0] = 'o' * width
        
    return '\n'.join(lines)
