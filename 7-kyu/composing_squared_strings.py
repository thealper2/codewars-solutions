def compose(s1, s2):
    lines1 = s1.split('\n')
    lines2 = s2.split('\n')
    n = len(lines1)
    new_lines = []
    for i in range(n):
        part1 = lines1[i][:i+1]
        part2_line = lines2[n - 1 - i]
        part2 = part2_line[:len(part2_line) - i] if i != 0 else part2_line
        new_line = part1 + part2
        new_lines.append(new_line)
    return '\n'.join(new_lines)
