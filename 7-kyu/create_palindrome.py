def solve(st):
    left = 0
    right = len(st) - 1
    
    while left < right:
        left_char = st[left]
        right_char = st[right]
        
        left_options = []
        if left_char == 'a':
            left_options.append('b')
        elif left_char == 'z':
            left_options.append('y')
        else:
            left_options.append(chr(ord(left_char) - 1))
            left_options.append(chr(ord(left_char) + 1))
        
        right_options = []
        if right_char == 'a':
            right_options.append('b')
        elif right_char == 'z':
            right_options.append('y')
        else:
            right_options.append(chr(ord(right_char) - 1))
            right_options.append(chr(ord(right_char) + 1))
        
        found = False
        for l in left_options:
            for r in right_options:
                if l == r:
                    found = True
                    break
            if found:
                break
        
        if not found:
            return False
        
        left += 1
        right -= 1
    
    return True