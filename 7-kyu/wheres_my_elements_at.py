def element_location(begin: int, end: int, index: int, size: int) -> int:
    """Returns the address of an element in an array.
    Raises an IndexError if the element is not in the array.
    
    Unlike normal Python behavior, negative indexes are still considered to
    to start from the beginning of the array and are thus always out of bounds.
    """
    if index < 0:
        raise IndexError("negative index")
    
    address = begin + index * size
    if address >= end:
        raise IndexError("address at or beyond end of array")
        
    return address
