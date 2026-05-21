from typing import Sequence


def restore_code(tokens: Sequence[Sequence[str]]) -> str:
    lines = []
    for token in tokens:
        if len(token) != 3:
            continue
        
        command = token[0]
        arg1 = token[1]
        arg2 = token[2]
        
        if not arg1.isalpha():
            continue
        
        is_valid_arg2 = False
        if arg2.isalpha():
            is_valid_arg2 = True
        elif arg2.lstrip('-').isdigit():
            is_valid_arg2 = True
        
        if not is_valid_arg2:
            continue
        
        if command == 'set':
            lines.append(f"{arg1}={arg2}")
        elif command == 'add':
            lines.append(f"{arg1}+={arg2}")
        elif command == 'sub':
            lines.append(f"{arg1}-={arg2}")
    
    if not lines:
        return ""
    
    return '\n'.join(lines)