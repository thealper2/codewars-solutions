def square_digits_sequence(n):
    seen = set()
    current = n
    length = 0
    
    while current not in seen:
        seen.add(current)
        length += 1
        current = sum(int(d) ** 2 for d in str(current))
        
    return length + 1