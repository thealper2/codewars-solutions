def equable_triangle(a,b,c):
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    
    perimeter = a + b + c
    semi_perimeter = perimeter / 2
    area_squared = (
        semi_perimeter
        * (semi_perimeter - a) 
        * (semi_perimeter - b) 
        * (semi_perimeter - c)
    )
        
    if area_squared <= 0:
        return False
    
    area = area_squared ** 0.5
    return abs(area - perimeter) < 1e-9