def wallpaper(l, w, h):
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
               "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
    
    if l == 0 or w == 0 or h == 0:
        return numbers[0]
    
    total_area = 2 * (l + w) * h
    required_area = total_area * 1.15 
    roll_area = 0.52 * 10
    
    rolls_needed = required_area / roll_area
    rolls_needed_rounded = int(rolls_needed) if rolls_needed == int(rolls_needed) else int(rolls_needed) + 1
    return numbers[rolls_needed_rounded]
