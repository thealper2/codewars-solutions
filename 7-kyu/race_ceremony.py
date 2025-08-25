def race_podium(blocks):
    first = (blocks + 2) // 3 + 1
    second = first - 1
    third = blocks - first - second
    if third == 0:
        third = 1
        second -= 1
        
    return (second, first, third)
