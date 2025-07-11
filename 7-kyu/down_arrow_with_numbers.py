def get_a_down_arrow_of(n):
    pattern = []
    for i in range(n):
        max_num = n - i
        line = []
        for num in range(1, max_num + 1):
            digit = num % 10
            line.append(str(digit))
        for num in range(max_num - 1, 0, -1):
            digit = num % 10
            line.append(str(digit))
        indented_line = ' ' * i + ''.join(line)
        pattern.append(indented_line)
    return '\n'.join(pattern)
