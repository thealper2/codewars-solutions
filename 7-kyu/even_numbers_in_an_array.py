def even_numbers(arr,n):
    return [item for item in arr if item % 2 == 0][-n:]
