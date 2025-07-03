def find_missing_number(sequence):
    parts = sequence.split()
    numbers = []
    for part in parts:
        if not part.lstrip('-').isdigit():
            return 1
        numbers.append(int(part))
    
    if not numbers:
        return 0
    
    unique_numbers = set(numbers)
    max_num = max(unique_numbers)
    if unique_numbers == set(range(1, max_num + 1)):
        return 0
    else:
        for i in range(1, max_num + 2):
            if i not in unique_numbers:
                return i
        return max_num + 1 