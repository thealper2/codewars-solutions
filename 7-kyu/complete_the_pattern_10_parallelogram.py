def pattern(n):
    if n <= 0:
        return ""
    
    number_str = "".join(str(i % 10) for i in range(1, n + 1))
    rows = []
    for i in range(n):
        leading_spaces = " " * (n - 1 - i)
        trailing_spaces = " " * i
        row = leading_spaces + number_str + trailing_spaces
        rows.append(row)
        
    return "\n".join(rows)
