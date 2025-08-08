def read(tape, head, moves):
    result = []
    n = len(tape)
    for move in moves:
        if move == '>':
            result.append(tape[head])
            head += 1
        elif move == '<':
            result.append(tape[head])
            head -= 1
            
    return ''.join(map(str, result))
