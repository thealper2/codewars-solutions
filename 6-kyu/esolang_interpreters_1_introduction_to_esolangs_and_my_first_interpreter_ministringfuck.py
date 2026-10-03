def my_first_interpreter(code):
    cell = 0
    output = []
    
    for command in code:
        if command == "+":
            cell = (cell + 1) % 256
        elif command == ".":
            output.append(chr(cell))
            
    return "".join(output)