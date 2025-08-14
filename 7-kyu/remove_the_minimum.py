def remove_smallest(numbers):
    if not numbers:
        return []
    a = numbers.copy()
    a.remove(min(a))
    return a
