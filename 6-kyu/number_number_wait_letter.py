import re

def do_math(st):
    tokens = []
    for idx, token in enumerate(st.split()):
        letter = re.search(r'[a-zA-Z]', token).group(0)
        number = int(re.sub(r'[a-zA-Z]', '', token))
        tokens.append((letter, number, idx))
        
    tokens.sort(key=lambda t: (t[0], t[2]))
    numbers = [t[1] for t in tokens]
    
    ops = ['+', '-', '*', '/']
    result = numbers[0]
    
    for i, num in enumerate(numbers[1:]):
        op = ops[i % 4]
        if op == '+':
            result += num
        elif op == '-':
            result -= num
        elif op == '*':
            result *= num
        else:
            result /= num
            
    return round(result)