def count_duplicates(name,age,height):
    seen = set()
    count = 0
    
    for a, b, c in zip(name, age, height):
        if (a, b, c) not in seen:
            seen.add((a, b, c))
        else:
            count += 1
            
    return count