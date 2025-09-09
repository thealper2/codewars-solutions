def type_of_triangle(a, b, c): 
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
        return 'Not a valid triangle'
    
    if a < b + c and b < c + a and c < a + b:
        if a == b and b == c and a == c:
            return 'Equilateral'
        elif a == b or b == c or a == c:
            return 'Isosceles'
        elif a != b and b != c and a != c:
            return 'Scalene'
        
    return 'Not a valid triangle'
