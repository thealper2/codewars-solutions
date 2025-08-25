def sort_transform(arr):
    def transform_two(arr):
        first_two = arr[:2]
        last_two = arr[-2:]
        combined = first_two + last_two
        return ''.join(chr(num) for num in combined)
    
    def sort_ascending(arr):
        sorted_arr = sorted(arr)
        return transform_two(sorted_arr)
    
    def sort_descending(arr):
        sorted_arr = sorted(arr, reverse=True)
        return transform_two(sorted_arr)
    
    def sort_ascii(arr):
        ascii_arr = [chr(num) for num in arr]
        sorted_ascii = sorted(ascii_arr)
        num_arr = [ord(char) for char in sorted_ascii]
        return transform_two(num_arr)
    
    part1 = transform_two(arr)
    part2 = sort_ascending(arr)
    part3 = sort_descending(arr)
    part4 = sort_ascii(arr)
    return f"{part1}-{part2}-{part3}-{part4}"
