def find_unique(numbers):
    seen = set()
    duplicates = set()

    for item in numbers:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    unique_items = list(seen - duplicates)
    return unique_items[0]