def pattern(n): 
    result = []
    for line in range(1, n + 1):
        spaces = ' ' * line
        number = line % 10
        numbers = (str(number) + ' ') * (n - line + 1)
        result.append(spaces + numbers.strip())
    return '\n'.join(result)