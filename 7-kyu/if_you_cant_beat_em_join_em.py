def cant_beat_so_join(numbers):
    sorted_numbers = sorted(numbers, key=sum, reverse=True)
    result = []
    for sub in sorted_numbers:
        result.extend(sub)
        
    return result
