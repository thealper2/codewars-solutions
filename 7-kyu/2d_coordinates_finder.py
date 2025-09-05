def find_coords(plane):
    lines = plane.split('\n')[::-1]
    coords = {}
    
    for j, line in enumerate(lines):
        for i, char in enumerate(line):
            if char.isdigit():
                coords[char] = (j, (i - j - 1) // 2)
    
    result = [coords[key] for key in sorted(coords.keys(), key=int)]
    return result
