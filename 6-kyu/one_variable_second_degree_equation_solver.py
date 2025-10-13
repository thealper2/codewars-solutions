def sec_deg_solver(a, b, c):
    def format_number(x):
        if x == 0:
            return "0.0"
        formatted = f"{x:.10f}"
        if '.' in formatted:
            formatted = formatted.rstrip('0')
            if formatted[-1] == '.':
                formatted += '0'
        return formatted
    
    if a == 0:
        if b == 0:
            if c == 0:
                return "The equation is indeterminate"
            else:
                return "Impossible situation. Wrong entries"
        else:
            solution = -c / b
            return f"It is a first degree equation. Solution: {format_number(solution)}"
    
    else:
        discriminant = b**2 - 4*a*c
        
        if discriminant < 0:
            return "There are no real solutions"
        elif discriminant == 0:
            solution = -b / (2*a)
            return f"It has one double solution: {format_number(solution)}"
        else:
            sqrt_d = discriminant**0.5
            solution1 = (-b - sqrt_d) / (2*a)
            solution2 = (-b + sqrt_d) / (2*a)
            solutions = sorted([solution1, solution2])
            return f"Two solutions: {format_number(solutions[0])}, {format_number(solutions[1])}"
